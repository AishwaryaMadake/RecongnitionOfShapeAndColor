
<html> 
    
    <!--fieldset style="height: 150%"-->
    <form action="" method="POST" enctype="multipart/form-data" >
        <link rel="stylesheet" href="webcss.css">
        <legend align = "center"><h2 style="color: black">Color And Shape Recognition</h2></legend>    
        <img style="margin-left: 150px; margin-top:30px" src="/gui/output.jpg">
         <button class="btn" name = "home" style=" padding: 10px 40px">Back To Home</button>
    </form>
    
    <!--/fieldset-->
    
    <?php

        if (isset($_POST['home']))
        {
            header('Location:/gui/web.html');
        }
        $file_pointer = 'countShape.txt'; 


        if (file_exists($file_pointer))  
        { 
            unlink("countShape.txt");
            unlink("countColor.txt");
            unlink("input.txt");

        } 
    ?>
    
    
</html>
