<?php

class JobTable extends Doctrine_Table{

  /**
   * Get the Job by its slug.
   * @param $slug
   * @return Job
   */
  public static function findJobBySlug($slug){
    return Doctrine_Query::create()
        ->from('Job j')->where('j.slug = ?', $slug)->fetchOne();
  }


}
