class xbmcvfs(object):
    def copy(self, source, destination):
        """Copy file to destination, returns true/false.

        source: string - file to copy.
        destination: string - destination file

        Example:
            success = xbmcvfs.copy(source, destination)"""
        return bool

    def delete(self, file):
        """Deletes a file.

        file: string - file to delete

        Example:
            xbmcvfs.delete(file)"""
        pass

    def rename(self, file, newFileName):
        """Renames a file, returns true/false.

        file: string - file to rename
        newFileName: string - new filename, including the full path

        Example:
            success = xbmcvfs.rename(file,newFileName)"""
        return bool
