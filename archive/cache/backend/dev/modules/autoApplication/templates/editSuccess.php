<?php use_helper('I18N', 'Date') ?>
<?php include_partial('application/assets') ?>

<div id="sf_admin_container">
  <h1><?php echo __('Edit Application', array(), 'messages') ?></h1>

  <?php include_partial('application/flashes') ?>

  <div id="sf_admin_header">
    <?php include_partial('application/form_header', array('application' => $application, 'form' => $form, 'configuration' => $configuration)) ?>
  </div>

  <div id="sf_admin_content">
    <?php include_partial('application/form', array('application' => $application, 'form' => $form, 'configuration' => $configuration, 'helper' => $helper)) ?>
  </div>

  <div id="sf_admin_footer">
    <?php include_partial('application/form_footer', array('application' => $application, 'form' => $form, 'configuration' => $configuration)) ?>
  </div>
</div>
