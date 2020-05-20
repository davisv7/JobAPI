TABLES = {}
TABLES['Config'] = (
    "CREATE TABLE `Config` ("
    "  `name` VARCHAR(32) NOT NULL,"
    "  `value` VARCHAR(32) NOT NULL,"
    "  PRIMARY KEY (`name`)"
    ") ENGINE=InnoDB")

TABLES['JobTemplate'] = (
    "CREATE TABLE `JobTemplate` ("
    "  `jobTemplateNme` VARCHAR(32) NOT NULL,"
    "  `jobTemplateVersion` INT,"

    "  `dynamicAllocation` BOOLEAN,"
    "  `initialExecutors` INT,"
    "  `minExecutors` INT,"
    "  `maxExecutors` INT,"
    "  `schedulerBacklogTimeout` INT,"
    "  `executorIdleTimeout` TIME,"

    "  `customConfigs` JSON,"
    "  `environmentVariables` JSON,"

    "  `applicationArtifactLocation` VARCHAR(32),"
    "  `defaultApplicationArguments` JSON,"
    "  `dependencyJars` JSON,"
    "  PRIMARY KEY (`jobTemplateNme`)"
    ") ENGINE=InnoDB")

TABLES['JobInstance'] = (
    "CREATE TABLE `JobInstance` ("
    "  `jobInstanceId` VARCHAR(32) NOT NULL,"
    "  `jobTemplateNme` VARCHAR(32) NOT NULL,"
    "  `jobTemplateVersion` INT,"
    "  `runDate` DATE,"
    "  `applicationArguments` JSON,"
    "  `status` VARCHAR(32),"
    "  PRIMARY KEY (`jobInstanceId`)"
    ") ENGINE=InnoDB")


################ stuff below may be useless ##############


class Config(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class JobTemplate(object):
    def __init__(self,
                 jobTemplateName,
                 jobTemplateVersion,
                 dynamicAllocation,
                 initialExecutors,
                 minExecutors,
                 maxExecutors,
                 scheduleBacklogYimeout,
                 executorIdleTimeout,
                 customConfigs,
                 environmentalVariables,
                 applicationArtifactLocation,
                 dependencyJars
                 ):
        self.jobTemplateName = jobTemplateName
        self.jobTemplateVersion = jobTemplateVersion
        self.dynamicAllocation = dynamicAllocation
        self.initialExecutors = initialExecutors
        self.minExecutors = minExecutors
        self.maxExecutors = maxExecutors
        self.scheduleBacklogYimeout = scheduleBacklogYimeout
        self.executorIdleTimeout = executorIdleTimeout
        self.customConfigs = customConfigs
        self.environmentalVariables = environmentalVariables
        self.applicationArtifactLocation = applicationArtifactLocation
        self.dependencyJars = dependencyJars


class JobInstance(object):
    def __init__(self, jobInstanceID,
                 jobTemplateName,
                 jobTemplateversion,
                 runDate,
                 applicationArguments,
                 status):
        self.jobInstanceID = jobInstanceID
        self.jobTemplateName = jobTemplateName
        self.jobTemplateversion = jobTemplateversion
        self.runDate = runDate
        self.applicationArguments = applicationArguments
        self.status = status
