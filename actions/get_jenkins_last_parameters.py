from lib import action


class GetLastJobParameters(action.JenkinsBaseAction):
    def run(self, job_name):
        last_build_number = self.jenkins.get_job_info(job_name)['lastCompletedBuild']['number']
        build_info_all = self.jenkins.get_job_info(job_name, last_build_number)['lastStableBuild']['actions']
        for p in build_info_all:
            if 'parameters' in p:
                build_info = p['parameters']
        build_parameters = ''
        for v in build_info:
            build_parameters = build_parameters + v['name'] + ':' + str(v['value']) + '\n'
        return build_parameters
