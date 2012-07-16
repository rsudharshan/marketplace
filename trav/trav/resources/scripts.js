$(document).ready(function() {   
  	 $('.fact').bind('click', function () {
      $.post("/test/"+this.id+"/", function(data) { 
          guess_result=data.fname+" " + data.lname;
          $('#result')[0].innerHTML="Hai ";
        $('#result')[0].innerHTML+=guess_result;
		});
			});
	 $('#login').bind('click', function () {
	 	usr=$('#usr').val()
	 	pwd=$('#pwd').val()
      $.post("/verify/",{username:usr,password:pwd}, function(data) { 
          if(data.status=="success")
          {
             window.location="/home"                                
          }
          if(data.status=="fail")
          {
          	 $('.content').html("Username or Password Incorrect, Login again");                                 

          }
         });
		});
		$('#signup').click(function(){
		usr=$('#id_username').val()
	 	fname=$('#id_firstname').val()
	 	lname=$('#id_lastname').val()
	 	pwd=$('#id_password').val()
	 	email=$('#id_email').val()
	 
	 $.post("/signup/",{username:usr,password:pwd,firstname:fname,lastname:lname,email:email}, function(data) {
         window.location="/update"
	 });
		});
});