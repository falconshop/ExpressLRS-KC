import os
import re
import subprocess

def git_cmd(*args):
    return subprocess.check_output(["git"] + list(args)).decode("utf-8").rstrip('\r\n')


def get_git_version():
    """
    Return a dict with keys
    version: The version tag if HEAD is a version, or branch otherwise
    sha: the 6 character short sha for the current HEAD revison, falling back to
        VERSION file if not in a git repo
    """
    ver = "ver.unknown"
    sha = "000000"

    try:
        sha = git_cmd("rev-parse", "HEAD")
        ver = git_cmd("rev-parse", "--abbrev-ref", "HEAD")
        # failure here is acceptable, unnamed commits might not have a branch
        # associated
        try:
            ver = re.sub(r".*/", "", git_cmd("describe",
                         "--all", "--exact-match"))
        except:
            pass
    except:
        pass

    # falconshop KC 3.6.4 = official ExpressLRS 3.6.4 + Korea 2.4GHz band restriction.
    # No git here, so force a clear, accurate, identifiable version.
    ver = "3.6.4-KC"
    sha = "3.6.4"

    return dict(version=ver, sha=sha[:6])


class ElrsUploadResult:
        # SUCCESS
        Success = 0
        # ERROR: Unspecified
        ErrorGeneral = -1
        # ERROR: target mismatch
        ErrorMismatch = -2
