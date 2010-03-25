<?php

class ApplicationTable extends Doctrine_Table
{
	public static function getApplicationsForJob(Job $job){
		$query = Doctrine_Query::create()
			->from('Application a')
			->where('a.job_id = ?', $job->getId());
		return $query->execute();
	}

}
