from StringIO import StringIO
from fabric.api import cd, env, run
from fabric.contrib.files import exists
from fabric.operations import sudo, put

def host_type():
    run('uname -s')

def bootstrap():
    """ bootstraps a new node """
    install_packages()

    if not exists("/app/workshop-php-bootstrap/"):
        run("mkdir -p /app/")
        with cd("/app/"):
            run("git clone git://github.com/bryanl/workshop-php-bootstrap.git")

    set_apache_config()


def install_packages():
    """ Install a bare minimum LAMP stack """
    run('apt-get install aptitude')
    run('aptitude update')
    run('aptitude upgrade -y')
    run('apt-get install -y -q debconf-utils')
    run('debconf-set-selections <<< "mysql-server mysql-server/root_password password jcQHbQjfEya27EHZ"')
    run('debconf-set-selections <<< "mysql-server mysql-server/root_password_again password jcQHbQjfEya27EHZ"')
    run('aptitude install -y -q mysql-server')
    run('aptitude install -y -q php5-mysql')
    run('aptitude install -y -q libapache2-mod-php5 php5 git')

def deploy():
    """ Deploy our app by pulling it from github """

    # NOTE: Python's "with" statement is a "context manager".
    # All the following commands  will be prefixed with "cd /path/to/  && "

    with cd("/app/workshop-php-bootstrap"):
        # Fetch & Merge from the remote repo
        run('git pull git://github.com/bryanl/workshop-php-bootstrap.git')

    set_file_permissions()

def set_file_permissions():
    """ Sets the appropriate read/execute permissions """
    with cd("/app/workshop-php-bootstrap/"):
        run("chmod -R 0755 clickapp/html")
        run("chown -R root:www-data clickapp/html")

def set_apache_config():
    """ Replace's apache's default config file """
    # Delete the existing default config file.
    if exists("/etc/apache2/sites-enabled/000-default.conf"):
        run("rm /etc/apache2/sites-enabled/000-default.conf")

    with cd("/etc/apache2/sites-enabled/"):
        run("ln -sf /app/workshop-php-bootstrap/support/apache/000-default.conf .")
        run("apachectl restart")

def backup():
    """ Make a tarball snapshot of the deployed codebase """
    with cd("/app/"):
        run("tar -czf /root/workshop-php-bootstrap.tgz workshop-php-bootstrap/")

def revert():
    """ Revert the codebase from a backup """
    if exists("/root/workshop-php-bootstrap.tgz"):
        with cd("/app/"):
            run("tar -xzf /root/workshop-php-bootstrap.tgz")

def db_setup(user='root', password='password'):
    """ set up a new database """

    cmd = "mysql -u %s -p%s -h localhost < /app/workshop-php-bootstrap/clickapp/db/db.sql" % (user, password)
    run(cmd)

    cmd = "mysql -u %s -p%s -h localhost myapp < /app/workshop-php-bootstrap/clickapp/db/myapp.sql" % (user, password)
    run(cmd)

    put(StringIO(
    '''
server = localhost
username = %s
password = %s
dbname = myapp
    ''' % (user, password)), '/app/workshop-php-bootstrap/clickapp/db.ini')
