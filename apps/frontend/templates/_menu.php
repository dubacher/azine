<div id="menuDiv">
<ul>
<?php
if($sf_user->isAuthenticated()){
    echo link_to("<li>".__('Home')."</li>",'homepage'); 
	echo link_to("<li>".__('Jobs')."</li>",'jobs'); 
	echo link_to("<li>".__('Post a new Job')."</li>",'job_new'); 
	echo link_to("<li>".__('Azine as your Agency')."</li>",'agency'); 
	echo link_to("<li>".__('Your Settings')."</li>",'sf_guard_settings'); 
	echo link_to("<li>".__('Logout')."</li>",'sf_guard_signout'); 
} else {
    echo link_to("<li>".__('Login')."</li>",'sf_guard_signin'); 
	echo link_to("<li>".__('Register')."</li>",'sf_guard_register'); 
} 
echo link_to("<li>".__('AGB')."</li>",'agb'); 
echo link_to("<li>".__('Contact')."</li>",'contact'); 
echo link_to("<li>".__('About')."</li>",'about'); 
?>
</ul>
</div>