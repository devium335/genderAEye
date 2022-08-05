Manual Data Setup
=================

Manual Data Setup is used if you have your own data set. For this to work tyour data must have:

a. Data text files with names matching the jpg image

b. The data files must have ``Male`` or ``Female`` on their seventh line


If the requirements are satisfied there are two steps

1. Sorting the images by gender

2. Putting them into data folders

.. _sorting_by_gender:

Sorting by Gender
-----------------

The function used for Gender Sorting is :py:func:`genderAEye.preprocessing.sort.sort_by_gender`

.. autofunction:: genderAEye.preprocessing.sort.sort_by_gender

Exception when the sorting gender has an invalid data file

.. autoexception:: genderAEye.preprocessing.exceptions.SortError

.. _sorting_data:

Sorting Data
------------

The function used for Data Sorting is :py:func:`genderAEye.preprocessing.sort.sort_to_data`

.. autofunction:: genderAEye.preprocessing.sort.sort_to_data