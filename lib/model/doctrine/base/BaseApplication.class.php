<?php

/**
 * BaseApplication
 * 
 * This class has been auto-generated by the Doctrine ORM Framework
 * 
 * @property integer $id
 * @property integer $job_id
 * @property integer $applicant_id
 * @property integer $requested_rate
 * @property string $rate_type
 * @property clob $application_text
 * @property blob $cv_attachment
 * @property sfGuardUser $User
 * @property Job $Job
 * 
 * @method integer     getId()               Returns the current record's "id" value
 * @method integer     getJobId()            Returns the current record's "job_id" value
 * @method integer     getApplicantId()      Returns the current record's "applicant_id" value
 * @method integer     getRequestedRate()    Returns the current record's "requested_rate" value
 * @method string      getRateType()         Returns the current record's "rate_type" value
 * @method clob        getApplicationText()  Returns the current record's "application_text" value
 * @method blob        getCvAttachment()     Returns the current record's "cv_attachment" value
 * @method sfGuardUser getUser()             Returns the current record's "User" value
 * @method Job         getJob()              Returns the current record's "Job" value
 * @method Application setId()               Sets the current record's "id" value
 * @method Application setJobId()            Sets the current record's "job_id" value
 * @method Application setApplicantId()      Sets the current record's "applicant_id" value
 * @method Application setRequestedRate()    Sets the current record's "requested_rate" value
 * @method Application setRateType()         Sets the current record's "rate_type" value
 * @method Application setApplicationText()  Sets the current record's "application_text" value
 * @method Application setCvAttachment()     Sets the current record's "cv_attachment" value
 * @method Application setUser()             Sets the current record's "User" value
 * @method Application setJob()              Sets the current record's "Job" value
 * 
 * @package    azine
 * @subpackage model
 * @author     DominikBusinger
 * @version    SVN: $Id: Builder.php 7294 2010-03-02 17:59:20Z jwage $
 */
abstract class BaseApplication extends sfDoctrineRecord
{
    public function setTableDefinition()
    {
        $this->setTableName('application');
        $this->hasColumn('id', 'integer', 6, array(
             'type' => 'integer',
             'primary' => true,
             'autoincrement' => true,
             'length' => '6',
             ));
        $this->hasColumn('job_id', 'integer', 6, array(
             'type' => 'integer',
             'notnull' => true,
             'length' => '6',
             ));
        $this->hasColumn('applicant_id', 'integer', 4, array(
             'type' => 'integer',
             'notnull' => true,
             'length' => '4',
             ));
        $this->hasColumn('requested_rate', 'integer', 6, array(
             'type' => 'integer',
             'length' => '6',
             ));
        $this->hasColumn('rate_type', 'string', 20, array(
             'type' => 'string',
             'default' => 'daily',
             'length' => '20',
             ));
        $this->hasColumn('application_text', 'clob', null, array(
             'type' => 'clob',
             'notnull' => true,
             ));
        $this->hasColumn('cv_attachment', 'blob', null, array(
             'type' => 'blob',
             ));

        $this->option('collate', 'utf8_unicode_ci');
        $this->option('charset', 'utf8');
    }

    public function setUp()
    {
        parent::setUp();
        $this->hasOne('sfGuardUser as User', array(
             'local' => 'applicant_id',
             'foreign' => 'id',
             'onDelete' => 'CASCADE'));

        $this->hasOne('Job', array(
             'local' => 'job_id',
             'foreign' => 'id',
             'onDelete' => 'CASCADE'));

        $timestampable0 = new Doctrine_Template_Timestampable();
        $this->actAs($timestampable0);
    }
}