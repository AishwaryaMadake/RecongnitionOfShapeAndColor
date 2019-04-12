<?php
    if(isset($_FILES['image'])){
      
      $file_name = $_FILES['image']['name'];
      file_put_contents('input.txt',$file_name); 
        
        
      $file_ext = substr( strrchr($file_name, '.'), 1);
      $extensions= array("jpg","png");      
      
      
   }
    
    
    if (isset($_POST['sub']))
    {
        if(empty($file_name)==true)
        {
           /* echo "<font size=5 face='cursive'>";
            echo '<font color="blue">';*/  
            echo "<script>alert( 'Please choose image first...');</script>";
            
        }
        else
            if(in_array($file_ext,$extensions)=== false)
            {
               /* echo "<font size=5 face='cursive'>";
                echo '<font color="blue">';*/
                echo   "<script>alert('This extension not allowed, please choose a jpg or png file.');</script>";
            }
      
      
        else
        {
            /*echo "<font size=5 face='cursive'>";
            echo '<font color="blue">';*/
            move_uploaded_file($_FILES["image"]["tmp_name"],
                                    "inputImages/" . $_FILES["image"]["name"]);
            echo "Success";
            header('Location:/gui/colorshape.php');
            ini_set('max_execution_time',1000);
            exec("python shape_color_recognition.py");
            
        }
         
        
    }
?>
<html>
    <head>
        <title>Color and Shape Recognition</title>
        <style>
        body {
                background-image: url("maxresdefault.jpg");
                background-repeat: no-repeat;
                background-size: cover;
           }
        </style>
    </head>

<body>
    <form action="" method="POST" enctype="multipart/form-data">
        <link rel="stylesheet" href="webcss.css">
        <div id=div class="shadowbox" style="top:100px ">
            <h1>Color and Shape Detection</h1>
            <input style="margin-top: 50px"; type="file" name="image" />
            <button class="btn" name = "sub" style=" margin-top: 20%; padding: 10px 40px">Submit</button>    
        </div>
    </form>       
 
             
</body>
</html>