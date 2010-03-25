<?php

/**
 * Application form base class.
 *
 * @method Application getObject() Returns the current form's model object
 *
 * @package    azine
 * @subpackage form
 * @author     DominikBusinger
 * @version    SVN: $Id: sfDoctrineFormGeneratedTemplate.php 24171 2009-11-19 16:37:50Z Kris.Wallsmith $
 */
abstract class BaseApplicationForm extends BaseFormDoctrine
{
  public function setup()
  {
    $this->setWidgets(array(
      'id'               => new sfWidgetFormInputHidden(),
      'job_id'           => new sfWidgetFormDoctrineChoice(array('model' => $this->getRelatedModelName('Job'), 'add_empty' => false)),
      'applicant_id'     => new sfWidgetFormDoctrineChoice(array('model' => $this->getRelatedModelName('User'), 'add_empty' => false)),
      'requested_rate'   => new sfWidgetFormInputText(),
      'rate_type'        => new sfWidgetFormInputText(),
      'application_text' => new sfWidgetFormTextarea(),
      'cv_attachment'    => new sfWidgetFormTextarea(),
      'created_at'       => new sfWidgetFormDateTime(),
      'updated_at'       => new sfWidgetFormDateTime(),
    ));

    $this->setValidators(array(
      'id'               => new sfValidatorDoctrineChoice(array('model' => $this->getModelName(), 'column' => 'id', 'required' => false)),
      'job_id'           => new sfValidatorDoctrineChoice(array('model' => $this->getRelatedModelName('Job'))),
      'applicant_id'     => new sfValidatorDoctrineChoice(array('model' => $this->getRelatedModelName('User'))),
      'requested_rate'   => new sfValidatorInteger(array('required' => false)),
      'rate_type'        => new sfValidatorString(array('max_length' => 20, 'required' => false)),
      'application_text' => new sfValidatorString(),
      'cv_attachment'    => new sfValidatorString(array('required' => false)),
      'created_at'       => new sfValidatorDateTime(),
      'updated_at'       => new sfValidatorDateTime(),
    ));

    $this->widgetSchema->setNameFormat('application[%s]');

    $this->errorSchema = new sfValidatorErrorSchema($this->validatorSchema);

    $this->setupInheritance();

    parent::setup();
  }

  public function getModelName()
  {
    return 'Application';
  }

}
