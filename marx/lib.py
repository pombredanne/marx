import glob
import json
import os


class Lib(object):
    """
    Object that allows access to the marx lib directory, for dynamic
    (and persistant) data.
    """

    def __init__(self, directory):
        """
        `directory' is a path (absolute) to the marx lib.
        """
        self.directory = directory

    def _json_listing(self, path):
        """
        List json files in path `path'
        """
        flag = ".json"
        for entry in glob.iglob(os.path.join(path, "*%s" % (flag))):
            entry = os.path.basename(entry)
            if entry.endswith(flag):
                entry = entry[:-len(flag)]
            yield entry

    def _file_listing(self, path):
        """
        """
        return os.listdir(path)

    def _load_json(self, path):
        """
        """
        return json.load(open(path, 'r'))

    def get_classes(self):
        """
        """
        return self._json_listing(os.path.join(self.directory, 'classes'))

    def get_class(self, what):
        """
        """
        return self._load_json(os.path.join(
            self.directory,
            'classes', "%s.json" % (what))
        )

    def get_containers(self):
        """
        """
        return self._json_listing(os.path.join(self.directory, 'containers'))

    def get_dockerfiles(self):
        """
        """
        return self._file_listing(os.path.join(self.directory, 'dockerfiles'))

    def get_config(self):
        """
        """
        return self._load_json(os.path.join(
            self.directory,
            "config.json"
        ))
