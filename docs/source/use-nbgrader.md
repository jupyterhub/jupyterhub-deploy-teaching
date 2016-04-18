## Using nbgrader

With the reference deployment, instructors can start to use nbgrader.
This section contains a rough sketch
of what that looks like. For full details see the [nbgrader
documentation](http://nbgrader.readthedocs.org/en/latest/).

To use nbgrader, an instructor will primarily use the nbgrader command line
program. Before doing this, the instructor will need to edit the
`nbgrader_config.py` file with a list of students and assignments as follows:

```python
c.NbGrader.db_assignments = [dict(name="ps1")]
c.NbGrader.db_students = [
    dict(id="bitdiddle", first_name="Ben", last_name="Bitdiddle"),
    dict(id="hacker", first_name="Alyssa", last_name="Hacker"),
    dict(id="reasoner", first_name="Louis", last_name="Reasoner")
]
```

You can also add an `email` field to each student and a `duedate` field to
each assignment. Each time you create a new assignment add it to the config
file.

For each assignment, first create a directory for an assignment's source:

	cd ~/nbgrader/<course>
	mkdir source/<assignment>

Next, copy notebooks into that directory:

	cp ~/Problem1.ipynb ~/nbgrader/<course>/source/<assignment>
	cp ~/Problem2.ipynb ~/nbgrader/<course>/source/<assignment>

These notebooks should be prepared using the nbgrader "Create Assignment Celltoolbar". Now create
the assignment:


	nbgrader assign <assignment>

That will create the student versions of the notebooks and put them into the
`~/nbgrader/<course>/release/<assignment>` directory with your solutions removed.

Next, release the assignment to students:

	nbgrader release <assignment>

At this point, students can fetch the assignment by doing:

	nbgrader fetch --course <course> <assignment>

That will give students a copy of the assignment directory with all of the notebooks. When students
are done working the notebooks, they can submit the assignment by doing:

	nbgrader submit --course <course> <assignment>

You can collect submitted assignments by doing:

	nbgrader collect <assignment>

This puts the students submitted work into the `~/nbgrader/<course>/submitted/<assignment>` directory. To enter those notebooks into the nbgrader web grading system, run:

	nbgrader autograde <assignment>

By default, this will rerun all of the students notebooks. If you don't want to run them:

	nbgrader autograde --no-execute <assignment>

To see the full command line options for nbgrader, run:

	nbgrader <subcommand> --help

Some other things you can do with nbgrader:

* Run `collect` and `autograde` commands for a single student or notebook.
* Collect a single assignment multiple times and regrade all or parts selectively.

