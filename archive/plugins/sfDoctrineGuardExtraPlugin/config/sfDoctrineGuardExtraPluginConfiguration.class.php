<?php

/*
 * This file is part of the symfony package.
 * (c) 2004-2006 Fabien Potencier <fabien.potencier@symfony-project.com>
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

/**
 * Plugin configuration class
 *
 * @package    symfony
 * @subpackage plugin
 * @author     Gordon Franke <gfranke@savedcite.com>
 * @version    SVN: $Id: sfDoctrineGuardExtraPluginConfiguration.class.php 23497 2009-11-01 17:21:30Z gimler $
 */
class sfDoctrineGuardExtraPluginConfiguration extends sfPluginConfiguration
{
  /**
   * @see sfPluginConfiguration
   */
  public function initialize()
  {
    if (sfConfig::get('app_sf_guard_extra_plugin_routes_register', true))
    {
      $this->dispatcher->connect(
        'routing.load_configuration',
        array(
          'sfGuardExtraRouting',
          'listenToRoutingLoadConfigurationEvent'
        )
      );
    }
  }
}