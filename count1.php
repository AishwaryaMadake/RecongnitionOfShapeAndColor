<?php

    if(isset($_POST['sub']))
    {
        header('Location:web.html');
    }
?>

<!DOCTYPE html>
<html>
    <link rel="stylesheet" href="webcss.css">
    <body>
        
        <form action="" method="POST" enctype="multipart/form-data">
            
            <?php
                $file = fopen("countShape.txt","r");
                $file1 = fopen("countColor.txt","r");

                echo "<font size=5 face='cursive'>";
                echo '<font color="blue">';
                echo "Shapewise Counting";
                echo "<br/>";
                while(! feof($file))
                {
                    echo "<font size=3 face='cursive'>";
                    echo '<font color="blue">';
                    echo fgets($file). "<br />";
                }
                fclose($file);
            
                echo "<font size=5 face='cursive'>";
                echo '<font color="blue">';
                echo "Colorwise Counting";
                echo "<br/>";
                while(! feof($file1))
                {
                    echo "<font size=3 face='cursive'>";
                    echo '<font color="blue">';
                    echo fgets($file1). "<br />";
                }
                fclose($file1);
                unlink("countShape.txt");
                unlink("countColor.txt");
                unlink("input.txt");
                unlink("output.jpg");
            ?>
        <button class="btn" name = "sub" style="padding: 10px 50px">Back to Home</button> 
        </form>
        </body>
</html>