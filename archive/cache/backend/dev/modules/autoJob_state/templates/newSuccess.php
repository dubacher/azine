<?php use_helper('I18N', 'Date') ?>
<?php include_partial('job_state/assets') ?>

<div id="sf_admin_container">
  <h1><?php echo __('New Job state', array(), 'messages') ?></h1>

  <?php include_partial('job_state/flashes') ?>

  <div id="sf_admin_header">
    <?php include_partial('job_state/form_header', array('job_state' => $job_state, 'form' => $form, 'configuration' => $configuration)) ?>
  </div>

  <div id="sf_admin_content">
    <?php include_partial('job_state/form', array('job_state' => $job_state, 'form' => $form, 'configuration' => $configuration, 'helper' => $helper)) ?>
  </div>

  <div id="sf_admin_footer">
    <?php include_partial('job_state/form_footer', array('job_state' => $job_state, 'form' => $form, 'configuration' => $configuration)) ?>
  </div>
</div>
