<td class="sf_admin_text sf_admin_list_td_id">
  <?php echo link_to($job->getId(), 'job_edit', $job) ?>
</td>
<td class="sf_admin_foreignkey sf_admin_list_td_state">
  <?php echo $job->getState() ?>
</td>
<td class="sf_admin_foreignkey sf_admin_list_td_user_id">
  <?php echo $job->getUserId() ?>
</td>
<td class="sf_admin_text sf_admin_list_td_title">
  <?php echo $job->getTitle() ?>
</td>
<td class="sf_admin_text sf_admin_list_td_description">
  <?php echo $job->getDescription() ?>
</td>
<td class="sf_admin_text sf_admin_list_td_attachment">
  <?php echo $job->getAttachment() ?>
</td>
<td class="sf_admin_text sf_admin_list_td_required_skills">
  <?php echo $job->getRequiredSkills() ?>
</td>
<td class="sf_admin_date sf_admin_list_td_start_date">
  <?php echo false !== strtotime($job->getStartDate()) ? format_date($job->getStartDate(), "f") : '&nbsp;' ?>
</td>
<td class="sf_admin_date sf_admin_list_td_end_date">
  <?php echo false !== strtotime($job->getEndDate()) ? format_date($job->getEndDate(), "f") : '&nbsp;' ?>
</td>
<td class="sf_admin_text sf_admin_list_td_fte">
  <?php echo $job->getFte() ?>
</td>
<td class="sf_admin_text sf_admin_list_td_slug">
  <?php echo $job->getSlug() ?>
</td>
<td class="sf_admin_date sf_admin_list_td_created_at">
  <?php echo false !== strtotime($job->getCreatedAt()) ? format_date($job->getCreatedAt(), "f") : '&nbsp;' ?>
</td>
<td class="sf_admin_date sf_admin_list_td_updated_at">
  <?php echo false !== strtotime($job->getUpdatedAt()) ? format_date($job->getUpdatedAt(), "f") : '&nbsp;' ?>
</td>
