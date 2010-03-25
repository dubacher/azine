<?php
/* run "php generate_test_jobs.php > 11_testJobs.yml" in this directory to generate a yml-file to import. */
 

$users = array('busi','dubi','ben');
$lorem = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Lorem ipsum dolor sit amet, consectetur adipisicing elit.";
$titles = array('Software Engineer','Technical Project Leader','Architect','Business Analyst','Labbersack','Test-Mänäger','Customer-Care','Sys-Admin');
$skills = array('Java','SQL','PHP','Lisp','WebSphere','Oracle','DB2','OO-Design','Web-Design','J2EE','Architecture');
$states = array('open','azined','canceled');

$yml = "Job:";
$i = 1;
$limit = 80;
while($i < $limit){
	$userIndex = $i%3;
	$titleIndex = $i%8;
	$stateIndex = $i%3;
	$skillIndex1 = ($i+1)%11;
	$skillIndex2 = ($i+2)%11;
	$skillIndex3 = ($i+3)%11;
	
	$yml .="
  job_$i:
    User:               ".$users[$userIndex]."
    title:              '".$titles[$titleIndex]."'
    description:        '".$i.$$titles[$titleIndex].$lorem."'
    JobState:           ".$states[$stateIndex]."
    required_skills:    '".$skills[$skillIndex1].", ".$skills[$skillIndex2].", ".$skills[$skillIndex3]."'";
	$i++;
}
echo $yml;
?>

