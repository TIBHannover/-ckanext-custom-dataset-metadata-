import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class CustomDatasetTypePlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IDatasetForm)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates/dataset_type')
        toolkit.add_public_directory(config_, 'public')
    

    def _custom_dataset_metadata(self, schema):
        schema.update({
            'dataset_type': [toolkit.get_converter('convert_to_extras')]
        })
        return schema

    def create_package_schema(self):
        schema = super(CustomDatasetTypePlugin, self).create_package_schema()
        schema = self._custom_dataset_metadata(schema)
        return schema

    def update_package_schema(self):
        schema = super(CustomDatasetTypePlugin, self).update_package_schema()
        schema = self._custom_dataset_metadata(schema)
        return schema

    def show_package_schema(self):
        schema = super(CustomDatasetTypePlugin, self).show_package_schema()
        schema.update({
            'dataset_type': [toolkit.get_converter('convert_from_extras')]
        })
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []
    
    