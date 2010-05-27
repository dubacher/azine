<?php

/**
 * Application filter form base class.
 *
 * @package    azine
 * @subpackage filter
 * @author     DominikBusinger
 * @version    SVN: $Id: sfDoctrineFormFilterGeneratedTemplate.php 24171 2009-11-19 16:37:50Z Kris.Wallsmith $
 */
abstract class BaseApplicationFormFilter extends BaseFormFilterDoctrine
{
  public function setup()
  {
    $this->setWidgets(array(
      'job_id'           => new sfWidgetFormDoctrineChoice(array('model' => $this->getRelatedModelName('Job'), 'add_empty' => true)),
      'applicant_id'     => new sfWidgetFormDoctrineChoice(array('model' => $this->getRelatedModelName('User'), 'add_empty' => true)),
      'requested_rate'   => new sfWidgetFormFilterInput(),
      'rate_type'        => new sfWidgetFormFilterInput(),
      'application_text' => new sfWidgetFormFilterInput(array('with_empty' => false)),
      'cv_attachment'    => new sfWidgetFormFilterInput(),
      'created_at'       => new sfWidgetFormFilterDate(array('from_date' => new sfWidgetFormDate(), 'to_date' => new sfWidgetFormDate(), 'with_empty' => false)),
      'updated_at'       => new sfWidgetFormFilterDate(array('from_date' => new sfWidgetFormDate(), 'to_date' => new sfWidgetFormDate(), 'with_empty' => false)),
    ));

    $this->setValidators(array(
      'job_id'           => new sfValidatorDoctrineChoice(array('required' => false, 'model' => $this->getRelatedModelName('Job'), 'column' => 'id')),
      'applicant_id'     => new sfValidatorDoctrineChoice(array('required' => false, 'model' => $this->getRelatedModelName('User'), 'column' => 'id')),
      'requested_rate'   => new sfValidatorSchemaFilter('text', new sfValidatorInteger(array('required' => false))),
      'rate_type'        => new sfValidatorPass(array('required' => false)),
      'application_text' => new sfValidatorPass(array('required' => false)),
      'cv_attachment'    => new sfValidatorPass(array('required' => false)),
      'created_at'       => new sfValidatorDateRange(array('required' => false, 'from_date' => new sfValidatorDateTime(array('required' => false, 'datetime_output' => 'Y-m-d 00:00:00')), 'to_date' => new sfValidatorDateTime(array('required' => false, 'datetime_output' => 'Y-m-d 23:59:59')))),
      'updated_at'       => new sfValidatorDateRange(array('required' => false, 'from_date' => new sfValidatorDateTime(array('required' => false, 'datetime_output' => 'Y-m-d 00:00:00')), 'to_date' => new sfValidatorDateTime(array('required' => false, 'datetime_output' => 'Y-m-d 23:59:59')))),
    ));

    $this->widgetSchema->setNameFormat('application_filters[%s]');

    $this->errorSchema = new sfValidatorErrorSchema($this->validatorSchema);

    $this->setupInheritance();

    parent::setup();
  }

  public function getModelName()
  {
    return 'Application';
  }

  public function getFields()
  {
    return array(
      'id'               => 'Number',
      'job_id'           => 'ForeignKey',
      'applicant_id'     => 'ForeignKey',
      'requested_rate'   => 'Number',
      'rate_type'        => 'Text',
      'application_text' => 'Text',
      'cv_attachment'    => 'Text',
      'created_at'       => 'Date',
      'updated_at'       => 'Date',
    );
  }
}
