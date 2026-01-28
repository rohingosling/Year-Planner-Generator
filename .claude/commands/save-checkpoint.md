# Save Checkpoint

Create a versioned checkpoint of the current project state.

## Actions

1. **Update documentation** (if changes warrant)
   - `CLAUDE.md` — Do's/Don'ts, project structure
   - `README.md` — Update to reflect current state of project
   - `docs/SPEC.md` — Product specification
   - `docs/ARCHITECTURE.md` — System design
   - `docs/CHANGELOG.md` — Add version entry with today's date
   - `docs/BACKLOG.md` — Update tasks and velocity metrics (see below)

2. **Update BACKLOG.md velocity metrics**
   - **Estimate size/effort** for any In Progress or Planned tasks missing values:
     | Size | Effort | Description |
     |------|--------|-------------|
     | XS | 1 | Trivial fix, config tweak, < 30 min |
     | S | 2 | Minor feature, single-file change, < 1 hour |
     | M | 3 | Modest feature, multi-file change, 1–3 hours |
     | L | 5 | Significant feature, new module, 3–6 hours |
     | XL | 8 | Major feature, architectural change, 6–12 hours |
     | XXL | 13 | Epic, multi-day effort (decomposition trigger) |
   - **Move completed tasks** from In Progress to Completed section with version number
   - **Update Daily Velocity table:**
     - Add row for today's date if not present
     - Update version range, task count, and effort for today
     - Recalculate **Total** (sum of all days)
     - Recalculate **Average** (total ÷ working days, exclude zero-task days)
     - Recalculate **Min** and **Max** (exclude zero-task days)
   - **Update Velocity Summary** phase totals if needed

3. **Increment version**
   - Update version in `CLAUDE.md` header
   - Update `config/config.yaml` document.version
   - Follow versioning rules: bug fix = minor bump, new section = minor bump

4. **Create backup**
   - Archive: `backup/year-planner-{version}-{YYYY-MM-DD}.zip`
   - Exclude: `backup/`, `.venv/`, `output/`, `__pycache__/`

## Backup Command

```powershell
powershell.exe -NoProfile -Command "
  $version = 'X.Y';
  $date = Get-Date -Format 'yyyy-MM-dd';
  $exclude = @('backup', '.venv', 'output', '__pycache__');
  $items = Get-ChildItem -Exclude $exclude;
  Compress-Archive -Path $items.FullName -DestinationPath \"backup/year-planner-$version-$date.zip\" -Force
"
```

## Checklist

- [ ] Documentation reflects current state
- [ ] Version numbers synchronized (CLAUDE.md, config.yaml)
- [ ] CHANGELOG.md updated with version entry and today's date
- [ ] BACKLOG.md: All tasks have size and effort estimates
- [ ] BACKLOG.md: Completed tasks moved with version number
- [ ] BACKLOG.md: Daily Velocity table updated (Total, Average, Min, Max)
- [ ] Backup created in `backup/`
