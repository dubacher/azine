<?php

/**
 * Job
 * 
 * This class has been auto-generated by the Doctrine ORM Framework
 * 
 * @package    azine
 * @subpackage model
 * @author     DominikBusinger
 * @version    SVN: $Id: Builder.php 7294 2010-03-02 17:59:20Z jwage $
 */
class Job extends BaseJob
{

  public function getAttachmentUrl(){
    $url =  "/".sfConfig::get('app_upload_dir_name').'/'.sfConfig::get('app_job_att_upload_dir')."/".$this->getAttachment();
    return $url;
  }
	
}