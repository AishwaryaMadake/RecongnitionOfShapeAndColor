<?php
    if ( ! empty( $_GET['msg'] ) )
    {
        $input=$_GET['msg'];
        file_put_contents('inputDraw.txt', $input); 
        $command = escapeshellcmd('speech37.py');
        $output = shell_exec($command);
        echo "<pre>$output</pre>";
        header('Refresh: 1; URL=speechRec.php');
    } 
    else
    {
        echo "Cannot recognize your voice...";
         header('Refresh: 2; URL=speechRec.php');
    }
    
?>