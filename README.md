This plugin is no longer used and merged in this extension:
https://github.com/TIBHannover/ckanext-crc1153

# ckanext-custom-dataset-metadata

Plugin custom_dataset_type:

Added custom dataset types to ckan dataset. Also, add a new facet section for filtering based on dataset type.


## Requirements


Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.8 and earlier | not tested    |
| 2.9             | Yes    |



## Installation


To install ckanext-custom-dataset-metadata:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

    git clone https://github.com//ckanext-custom-dataset-metadata.git
    cd ckanext-custom-dataset-metadata
    pip install -e .
	pip install -r requirements.txt

3. Add `custom_dataset_type` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload

