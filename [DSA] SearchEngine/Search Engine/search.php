<?php
include("config.php");
include("SiteResultsProvider.php");
include("environmentVariables.php");

if(isset($_GET["term"]))
  {
    $term = $_GET["term"];
  }
  else{
      exit("You must enter a search term");
  }  

  $type = isset($_GET["type"]) ? $_GET["type"] : "sites";

?>


<!DOCTYPE html>
<html>
<head>

    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Pack Engine</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="design/style.css" />
    <script src="main.js"></script>
</head>
<body>
    <div class = "wrapper">
    
        <div class="header">
            <div class = "headerContent">
            <div class = "logoContainer">
            <a href="index.php">
                 <img src ="design/imgs/logo.png">
            </a>
            </div>
            <div class ="searchContainer">

                <form action="search.php" method = "GET">

                    <div class="searchBarContainer">
                        <input class = "searchBox" type = "text" name = "term">
                        <button class = "searchButton"> 
                            <img src = "design/imgs/magnify.png">
                        </button>
                    </div>

                </form>


            </div>

        </div>
            <div class ="tabsContainer">
                <ul class ="tabList">
                    <li class="<?php echo $type == 'sites' ? 'active':'' ?>">
                        <a href='<?php echo "search.php?term=$term&type=sites;" ?>'>
                        Sites
                            </a>

                    </li>    

                </ul>

            </div>
         </div>
            <div class="mainResultsSection">
                <?php
                $resultsProvider = new SiteResultsProvider($con);
                $numResults = $resultsProvider->getNumResults($term);
                echo "<p class='resultsCount'>$numResults results found </p>";
                echo $resultsProvider->getResultsHtml($term);
               ?>

            </div>


    
    </div>

    
</body>
</html>

<!-- this is jquery , ye javascript ki library ha . javascript sa bhe kam hoata par jquery can make your life easier 

 hum na dakha k html file directly href ma open ni horahi thi because of php. Php just php i file redirect karta ha  . untill and unless usko proper file
 redirection na di jae . to eslia mana javascript and jquery ki help li 

  eb her  link ka apna href hota ha  and in order to identify each anchor tag hama usko aik unique name dana hoga . 
  q k agar sab anchor tags ka same name hogaya to jab hum click karainga to kasa pata chala ga k konsa anchor pa click hua
  it is same as 10 bando ka name haseeb hoga to kasa pata chalaga k kis haseeb ko bulaya . 

  to eslia mana her ancho tag ko aik unique id da di .. like haseeb 1 haseeb 2 and etc . 
  eb  her anchor tag par onclick ka event laga dia and usi tag ki id pass kar di . k jab es specific anchor pa click  ho to es function ko es anchor ki id pass kar do 
  taqay pata chal jae k kis id wala anchor ko click kea . 
to usi id ki base par mana uska href get kea and redirect karwa dia :P 

let me know agar smjh na ae . to ma dosra tareka sa smjhao :) agy ha thanks ab ye har link p work kry ga? yes
ye is wali if statement ma wo code nai dala? nah same copy paste kar dain hojaega kam.wo script to ni krni na? nahi scripe just aik page pa rahaga . 
jis jis page par asay achor print hoga us pa jquery ya javascript zarori hogi par looks like apka ye aik he page ha hmm
untitled kya scene hA?

untitled ?
ye dkhna


 -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.js"></script>
<script>

function redirection(id,event){
    event.preventDefault();
    //window.open($("#"+id).attr("href"), 'newwindow', 'width=350, height=450, top=200, left=500'); return false;
    $('#'+id).attr('href',$('#'+id).attr('href').replace('C:',<?php echo "'".$baseUrl."'"; ?>));

    window.location=$('#'+id).attr('href');
}

</script>