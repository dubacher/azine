<td colspan="13">
  <?php echo __('%%id%% - %%state%% - %%user_id%% - %%title%% - %%description%% - %%attachment%% - %%required_skills%% - %%start_date%% - %%end_date%% - %%fte%% - %%slug%% - %%created_at%% - %%updated_at%%', array('%%id%%' => link_to($job->getId(), 'job_edit', $job), '%%state%%' => $job->getState(), '%%user_id%%' => $job->getUserId(), '%%title%%' => $job->getTitle(), '%%description%%' => $job->getDescription(), '%%attachment%%' => $job->getAttachment(), '%%required_skills%%' => $job->getRequiredSkills(), '%%start_date%%' => false !== strtotime($job->getStartDate()) ? format_date($job->getStartDate(), "f") : '&nbsp;', '%%end_date%%' => false !== strtotime($job->getEndDate()) ? format_date($job->getEndDate(), "f") : '&nbsp;', '%%fte%%' => $job->getFte(), '%%slug%%' => $job->getSlug(), '%%created_at%%' => false !== strtotime($job->getCreatedAt()) ? format_date($job->getCreatedAt(), "f") : '&nbsp;', '%%updated_at%%' => false !== strtotime($job->getUpdatedAt()) ? format_date($job->getUpdatedAt(), "f") : '&nbsp;'), 'messages') ?>
</td>
