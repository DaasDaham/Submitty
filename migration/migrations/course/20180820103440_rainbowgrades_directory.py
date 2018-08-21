import os
import grp
from pathlib import Path


def up(config, conn, semester, course):
    course_dir = Path(config.submitty['submitty_data_dir'], 'courses', semester, course)
    course_customization_dir = Path(course_dir, 'uploads', 'rainbow_grades')

    # create the directories
    os.makedirs(str(course_customization_dir), exist_ok=True)

    php_user = config.submitty_users['php_user']

    # get course group
    stat_info = os.stat(str(course_dir))
    course_group_id = stat_info.st_gid
    course_group = grp.getgrgid(course_group_id)[0]

    # set the owner/group/permissions
    os.system("chown -R "+php_user+":"+course_group+" "+str(course_customization_dir))
    os.system("chmod -R u+rwx  "+str(course_customization_dir))
    os.system("chmod -R g+rwxs "+str(course_customization_dir))
    os.system("chmod -R o-rwx  "+str(course_customization_dir))

    pass


def down(config, conn, semester, course):
    pass