<?php

/**
 * Job form.
 *
 * @package    azine
 * @subpackage form
 * @author     DominikBusinger
 * @version    SVN: $Id: sfDoctrineFormTemplate.php 23810 2009-11-12 11:07:44Z Kris.Wallsmith $
 */
class JobForm extends BaseJobForm
{
  public function configure() {
  	parent::configure();
  	    
  	$this->setValidator('slug', new sfValidatorNumber(array('required' => false)));
    $this->setValidator('created_at', new sfValidatorNumber(array('required' => false)));
    $this->setValidator('updated_at', new sfValidatorNumber(array('required' => false)));

    $this->validatorSchema['attachment'] = new sfValidatorFile(array(
	  'required'   => false,
	  'path'       => sfConfig::get('sf_upload_dir').'/'.sfConfig::get('app_job_att_upload_dir'),
	  'mime_types' => sfConfig::get('app_job_att_mime_types'),
	));    
    $this->setWidget('attachment', new sfWidgetFormInputFile());
  }
	}
