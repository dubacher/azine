<h1><?php echo $job->getTitle() ?></h1>

<table>
  <tbody>
    <tr>
      <th><?php echo __('State'); ?></th>
      <td><?php echo $job->getState() ?></td>
    </tr>
    <tr>
      <th><?php echo __('Description'); ?></th>
      <td><?php echo $job->getDescription() ?></td>
    </tr>
<?php if( $job->getAttachment() != null){ ?>
    <tr>
      <th><?php echo __('Attachment'); ?></th>
      <td><a href="<?php echo $job->getAttachmentUrl() ?>">Download Attachment.</a></td>
    </tr>
<?php } ?>
    <tr>
      <th><?php echo __('Required skills'); ?></th>
      <td><?php echo $job->getRequiredSkills() ?></td>
    </tr>
    <tr>
      <th><?php echo __('Updated at'); ?></th>
      <td><?php echo $job->getUpdatedAt() ?></td>
    </tr>
    <tr>
  </tbody>
</table>
<?php 
if($editable){
?> 
<div id="jobEditButtonsDiv">
	<?php echo link_to(__('Edit Job'),'job_update',array('slug' => $job->getSlug())); ?>
	<?php echo link_to(__('New Job'),'job_new'); ?> 
<div id="jobApplicationsDiv">

</div>
} else {
	echo link_to(__('Apply for this Job'), array('slug'=> $job->getSlug()));
}
?>
