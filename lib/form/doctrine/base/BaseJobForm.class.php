<?php

/**
 * Job form base class.
 *
 * @method Job getObject() Returns the current form's model object
 *
 * @package    azine
 * @subpackage form
 * @author     DominikBusinger
 * @version    SVN: $Id: sfDoctrineFormGeneratedTemplate.php 24171 2009-11-19 16:37:50Z Kris.Wallsmith $
 */
abstract class BaseJobForm extends BaseFormDoctrine
{
  public function setup()
  {
    $this->setWidgets(array(
      'id'              => new sfWidgetFormInputHidden(),
      'state'           => new sfWidgetFormDoctrineChoice(array('model' => $this->getRelatedModelName('JobState'), 'add_empty' => false)),
      'user_id'         => new sfWidgetFormDoctrineChoice(array('model' => $this->getRelatedModelName('User'), 'add_empty' => false)),
      'title'           => new sfWidgetFormInputText(),
      'description'     => new sfWidgetFormTextarea(),
      'attachment'      => new sfWidgetFormInputText(),
      'required_skills' => new sfWidgetFormInputText(),
      'start_date'      => new sfWidgetFormDate(),
      'end_date'        => new sfWidgetFormDate(),
      'fte'             => new sfWidgetFormInputText(),
      'slug'            => new sfWidgetFormInputText(),
      'created_at'      => new sfWidgetFormDateTime(),
      'updated_at'      => new sfWidgetFormDateTime(),
    ));

    $this->setValidators(array(
      'id'              => new sfValidatorDoctrineChoice(array('model' => $this->getModelName(), 'column' => 'id', 'required' => false)),
      'state'           => new sfValidatorDoctrineChoice(array('model' => $this->getRelatedModelName('JobState'))),
      'user_id'         => new sfValidatorDoctrineChoice(array('model' => $this->getRelatedModelName('User'))),
      'title'           => new sfValidatorString(array('max_length' => 200)),
      'description'     => new sfValidatorString(),
      'attachment'      => new sfValidatorString(array('max_length' => 255, 'required' => false)),
      'required_skills' => new sfValidatorString(array('max_length' => 255, 'required' => false)),
      'start_date'      => new sfValidatorDate(),
      'end_date'        => new sfValidatorDate(array('required' => false)),
      'fte'             => new sfValidatorInteger(array('required' => false)),
      'slug'            => new sfValidatorString(array('max_length' => 255, 'required' => false)),
      'created_at'      => new sfValidatorDateTime(),
      'updated_at'      => new sfValidatorDateTime(),
    ));

    $this->validatorSchema->setPostValidator(
      new sfValidatorDoctrineUnique(array('model' => 'Job', 'column' => array('slug')))
    );

    $this->widgetSchema->setNameFormat('job[%s]');

    $this->errorSchema = new sfValidatorErrorSchema($this->validatorSchema);

    $this->setupInheritance();

    parent::setup();
  }

  public function getModelName()
  {
    return 'Job';
  }

}
