<?php
class SiteResultsProvider {
    private $con;
    public function __construct($con)
    {
        $this->con = $con;

    }
    public function getNumResults($term){
        $query = $this->con->prepare("SELECT COUNT(*) as total 
                                       FROM documents WHERE docID in (SELECT docID FROM contents WHERE MATCH(content) AGAINST
                                       (:term IN BOOLEAN MODE))");
        
        $searchTerm = "+".$term;
        $query->bindParam(":term",$term);
        $query->execute();

        $row = $query->fetch(PDO::FETCH_ASSOC);
        return $row["total"];
    }
    public function getResultsHTML($term)
    {
        $term_ = explode(" ",$term);
        $term__ = $term;
        $term__ = preg_replace('/\s+/', '|', $term__);
        if(sizeOf($term_) > 1)
        {
            $empty = "";
            foreach($term_ as $t)
            {
                $empty .=" +".$t; 
            }
            //echo $term__;
            $query = $this->con->prepare(" SELECT title,path 
            FROM documents WHERE title = '$term'
            UNION
            SELECT title,path 
            FROM documents WHERE title REGEXP '$term__'
            UNION
            SELECT title,path from documents WHERE docID in (SELECT docID from contents 
            WHERE MATCH(content) AGAINST (:term in BOOLEAN MODE))");
            $searchTerm = $term;
            $query->bindParam(":term",$empty);
            $query->execute();
            $resultsHtml = "<div class = 'siteResults'>";
            $index=0;
            while($row = $query->fetch(PDO::FETCH_ASSOC))
            {
                $title = $row["title"];
                $path = $row["path"];
                $resultsHtml.="<div class='resultContainer'>
                        <h3 class='title'>
                        <a class='result' id='link_".$index."' onclick='redirection(this.id,event)' href='$path' target='_blank'>
                        $title
                        </a>

                        </h3>
                        <span class='path'>$path</span>
            
            </div>";
            
           
            $index++;
            
            } 
            $resultsHtml.="</div>";
            return $resultsHtml;

        }//iski jaga tha wo test k lye dala tha.. done . 
        /**SELECT title,path 
            FROM documents WHERE title = '$term'
            UNION
            SELECT title,path 
            FROM documents WHERE title like '%$term%'
            UNION  
            select t1.path,t1.title from
            (select documents.docid,title,path,t.frequency from documents as t1 join 
            (select words.docid ,frequency from words where match (word) against(:term in boolean mode)) as t on t.docid = t1.docID order by t1.frequency desc) 
            <a class='result' id='link_".$index."'  href='". header('Location:Array.html')."' target='_blank'>*/
        else
        {

            // jo keyword search hota ha wo kis parameter ma ata ha ?
            
            $query = $this->con->prepare("
            (select distinct title, path,frequency from documents join 
            (select words.docid ,frequency from words where match (word) against(:term in boolean mode)) as t on t.docid = documents.docID order by
  	  
 CASE
        WHEN title LIKE '%".$term."' OR title LIKE '".$term."%' THEN 1
 END desc
 ,
 frequency
 desc


)
 
 
            LIMIT 0,50");
            $searchTerm = $term;
            $query->bindParam(":term",$term);
            $query->execute();
            $resultsHtml = "<div class = 'siteResults'>";
            $index=0;
            while($row = $query->fetch(PDO::FETCH_ASSOC))
            {
                $title = $row["title"];
                $path = $row["path"];
                $resultsHtml.="<div class='resultContainer'>
                        <h3 class='title'>
                          <a class='result' id='link_".$index."' onclick='redirection(this.id,event)' href='$path' target='_blank'>
                          
                            $title
                            </a>

                        </h3>
                        <span class='path'>$path</span>
            
            </div>";
            
           
       
            $index++;
            } 
            $resultsHtml.="</div>";
            return $resultsHtml;
            
            
            



            
            }
            



            
           

    
    
           
        }
    }
        
        
        





?>