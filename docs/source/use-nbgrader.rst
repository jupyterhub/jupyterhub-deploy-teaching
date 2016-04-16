Using nbgrader
==============

With the reference deployment, instructors can start to use nbgrader.
This section contains a rough sketch
of what that looks like. For full details see the `nbgrader
documentation <http://nbgrader.readthedocs.org/en/latest/>`_.

Preparing class assignments - Instructor
----------------------------------------
To use nbgrader, an instructor will primarily use the nbgrader command line
program.

Create a list of students and assignments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Before doing this, the instructor will need to edit the
:file:`nbgrader_config.py` file with a list of students and assignments as
follows:

.. code:: python

    c.NbGrader.db_assignments = [dict(name="ps1")]
    c.NbGrader.db_students = [
        dict(id="bitdiddle", first_name="Ben", last_name="Bitdiddle"),
        dict(id="hacker", first_name="Alyssa", last_name="Hacker"),
        dict(id="reasoner", first_name="Louis", last_name="Reasoner")
    ]

You can also add an ``email`` field to each student and a ``duedate`` field to
each assignment.

Remember to add new assignments to the :file:`nbgrader_config.py` file as the
assignments are created.

Create an assignment directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Create a directory for each assignment's source::

	$ cd ~/nbgrader/<course>
	$ mkdir source/<assignment>

Copy notebooks into assignment directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Copy notebooks into the assignment directory::

	$ cp ~/Problem1.ipynb ~/nbgrader/<course>/source/<assignment>
	$ cp ~/Problem2.ipynb ~/nbgrader/<course>/source/<assignment>

Create a student version of an assignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
These notebooks should be prepared using the nbgrader
"Create Assignment Celltoolbar". Now create the assignment::

    $ nbgrader assign <assignment>

After creating the student versions of the notebooks, put them into the
:file:`~/nbgrader/<course>/release/<assignment>` directory, and remember
to remove your solutions.

Release the assignment
~~~~~~~~~~~~~~~~~~~~~~
Next, release the assignment to students::

	$ nbgrader release <assignment>


Working with an assignment - Students
-------------------------------------

Fetch the assignment
~~~~~~~~~~~~~~~~~~~~
At this point, students can fetch the assignment by doing::

	$ nbgrader fetch --course <course> <assignment>

That will give students a copy of the assignment directory with all of the
notebooks.

Submit an assignment solution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When students are done working the notebooks, they can submit the assignment
by doing::

	$ nbgrader submit --course <course> <assignment>

Grading the assignments - Instructor
------------------------------------

Collect student assignments
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can collect submitted assignments by doing::

	$ nbgrader collect <assignment>

This puts the students submitted work into the
:file:`~/nbgrader/<course>/submitted/<assignment>` directory.

Grade the assignments
~~~~~~~~~~~~~~~~~~~~~
To enter those notebooks into the nbgrader web grading system, run::

	$ nbgrader autograde <assignment>

By default, this will rerun all of the students notebooks.

If you don't want to run them::

	$ nbgrader autograde --no-execute <assignment>

Next steps
----------
To see the full command line options for nbgrader, run::

	$ nbgrader <subcommand> --help

Some other things you can do with nbgrader:

* Run :command:`collect` and :command:`autograde` commands for a single
  student or notebook.
* Collect a single assignment multiple times and regrade all or parts
  selectively.

