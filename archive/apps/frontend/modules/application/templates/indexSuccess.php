<h1>Applications List</h1>

<table>
  <thead>
    <tr>
      <th>Id</th>
      <th>Job</th>
      <th>Applicant</th>
      <th>Requested rate</th>
      <th>Rate type</th>
      <th>Application text</th>
      <th>Cv attachment</th>
      <th>Created at</th>
      <th>Updated at</th>
    </tr>
  </thead>
  <tbody>
    <?php foreach ($applications as $application): ?>
    <tr>
      <td><a href="<?php echo url_for('application/edit?id='.$application->getId()) ?>"><?php echo $application->getId() ?></a></td>
      <td><?php echo $application->getJobId() ?></td>
      <td><?php echo $application->getApplicantId() ?></td>
      <td><?php echo $application->getRequestedRate() ?></td>
      <td><?php echo $application->getRateType() ?></td>
      <td><?php echo $application->getApplicationText() ?></td>
      <td><?php echo $application->getCvAttachment() ?></td>
      <td><?php echo $application->getCreatedAt() ?></td>
      <td><?php echo $application->getUpdatedAt() ?></td>
    </tr>
    <?php endforeach; ?>
  </tbody>
</table>

  <a href="<?php echo url_for('application/new') ?>">New</a>
