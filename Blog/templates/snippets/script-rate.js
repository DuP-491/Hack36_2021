
function rate5(){ 
    document.getElementById("5").style.color = "orange"; 
        document.getElementById("4").style.color = "orange";
      document.getElementById("3").style.color = "orange";
      document.getElementById("2").style.color = "orange"; 
     document.getElementById("1").style.color = "orange";
     }
    
   function rate4(){
      document.getElementById("5").style.color = "#9e9e9e"; 
        document.getElementById("4").style.color = "orange";
      document.getElementById("3").style.color = "orange";
      document.getElementById("2").style.color = "orange"; 
     document.getElementById("1").style.color = "orange";
   }
   
   function rate3(){
      document.getElementById("5").style.color = "#9e9e9e"; 
        document.getElementById("4").style.color = "#9e9e9e";
      document.getElementById("3").style.color = "orange";
      document.getElementById("2").style.color = "orange"; 
     document.getElementById("1").style.color = "orange";
   }
   
   function rate2(){
      document.getElementById("5").style.color = "#9e9e9e"; 
        document.getElementById("4").style.color = "#9e9e9e";
      document.getElementById("3").style.color = "#9e9e9e";
      document.getElementById("2").style.color = "orange"; 
     document.getElementById("1").style.color = "orange";
   }
   
   function rate1(){
      document.getElementById("5").style.color = "#9e9e9e"; 
        document.getElementById("4").style.color = "#9e9e9e";
      document.getElementById("3").style.color = "#9e9e9e";
      document.getElementById("2").style.color = "#9e9e9e";
     document.getElementById("1").style.color = "orange";
   }
   
   document.getElementById("5").onclick = function(){
     rate5();
   }
   document.getElementById("4").onclick = function(){
     rate4();
   }
   document.getElementById("3").onclick = function(){
     rate3();
   }
   document.getElementById("2").onclick = function(){
     rate2();
   }
   document.getElementById("1").onclick = function(){
     rate1();
   }
   
   
   