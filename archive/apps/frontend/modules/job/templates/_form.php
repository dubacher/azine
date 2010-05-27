<?php use_stylesheets_for_form($form) ?>
<?php use_javascripts_for_form($form) ?>
<?php $job = $form->getObject(); ?>
<form
    action="<?php echo url_for('job_'.($job->isNew() ? 'new' : 'update'), array('slug'=>$job->getSlug())) ?>"
    method="post"
    <?php $form->isMultipart() and print 'enctype="multipart/form-data" ' ?>>
<?php if (!$form->getObject()->isNew()): ?>
<input type="hidden" name="sf_method" value="put" />
<?php endif; ?>
  <table>
    <tfoot>
      <tr>
        <td colspan="2">
          <?php echo $form->renderHiddenFields(false) ?>
          &nbsp;<a href="<?php echo url_for('job/index') ?>">Back to list</a>
          <?php 
            if ($form->getObject()->isNew()){
              echo link_to(__('Cancel'), 'jobs');
            } else {
              echo link_to(__('Cancel'), 'job_show', array('slug'=>$form->getObject()->getSlug()));
              echo "&nbsp;";
              echo link_to(__('Delete'), 'job_delete', array('slug'=>$form->getObject()->getSlug()), array( 'method' => 'delete', 'confirm' =>__('Do you want to delete this job?')));
            }
           ?>
          <input type="submit" value="Save" />
        </td>
      </tr>
    </tfoot>
    <tbody>
      <?php echo $form->renderGlobalErrors() ?>
      <tr>
        <th><?php echo $form['state']->renderLabel() ?></th>
        <td>
          <?php echo $form['state']->renderError() ?>
          <?php echo $form['state'] ?>
        </td>
      </tr>
      <tr>
        <th><?php echo $form['title']->renderLabel() ?></th>
        <td>
          <?php echo $form['title']->renderError() ?>
          <?php echo $form['title'] ?>
        </td>
      </tr>
      <tr>
        <th><?php echo $form['description']->renderLabel() ?></th>
        <td>
          <?php echo $form['description']->renderError() ?>
          <?php echo $form['description'] ?>
        </td>
      </tr>
      <tr>
        <th><?php echo $form['attachment']->renderLabel() ?></th>
        <td>
          <?php echo $form['attachment']->renderError() ?>
          <?php echo $form['attachment'] ?>
        </td>
      </tr>
      <tr>
        <th><?php echo $form['required_skills']->renderLabel() ?></th>
        <td>
          <?php echo $form['required_skills']->renderError() ?>
          <?php echo $form['required_skills'] ?>
        </td>
      </tr>
    </tbody>
  </table>
</form>
