function validusername(){
    // email validation : 
     var usernameField=document.getElementById("usernameField");
     var usernameError=document.getElementById("usernameError");
     if (usernameField.value.length < 8) {  
             // phone number should starts with 6 to 9 between only 
             usernameError.innerHTML="Username should be more than 8 characters ";
             usernameError.style.color="red";
             return false;
     } 
     usernameError.innerHTML=""; // CLEAR ERROR MESSAGE.. 
  
  } 
  function validemail(){
  
     var emailField=document.getElementById("emailField");
     var emailError=document.getElementById("emailError");   
     if(emailField.value==""){
             emailError.innerHTML="  Email is Required... ";
             emailError.style.color="red";
             return false;
     }
     else if(!emailField.value.match(/[a-zA-Z0-9/-/.]*[@][ga][a-z]{3,4}[/.][comin]{2,3}$/)){
             emailError.innerHTML="Please enter a valid email";
             emailError.style.color="red";
             return false;
     } 
     emailError.innerHTML=""; // CLEAR ERROR MESSAGE.. 
  }
  function validpassword(){
     var passwordField=document.getElementById("passwordField");
     var passwordError=document.getElementById("passwordError");
    // password validation :
    if(passwordField.value==""){
         passwordError.innerHTML="Password Required... ";
         passwordError.style.color="red";
         return false;
     }
     else if (passwordField.value.search(/^(?=.*?[A-Z])(?=(.*[a-z]){1,})(?=(.*[\d]){1,})(?=(.*[\W]){1,})(?!.*\s).{8,}$/) < 0) {
         passwordError.innerHTML="Password should contain 1 uppercase,1 special,1 digit and should be more than 8 characters";
          passwordError.style.color="red";
         return false;
     }
  
     passwordError.innerHTML=""; // CLEAR THE ERROR MESSAGE.. 
  
  }
      document.querySelector('.img__btn').addEventListener('click', function() {
    document.querySelector('.cont').classList.toggle('s--signup');
  });