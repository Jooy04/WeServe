ft_call='''
CREATE TABLE IF NOT EXISTS staging.ft_call(
    callID INTEGER PRIMARY KEY NOT NULL
    , callerID INTEGER NOT NULL
    , agentID INTEGER NOT NULL
    , assignedTo" INTEGER NOT NULL
    , callDurationInSeconds INTEGER NOT NULL
    ,resolutionDurationInHours" INTEGER NOT NULL
);
'''

dim_caller= '''
CREATE TABLE IF NOT EXISTS staging.dim_caller(
    callerID INTEGER PRIMARY KEY NOT NULL
    , callType VARCHAR(255) NOT NULL
    , complaintTopic TEXT NOT NULL
    , status VARCHAR(255) NOT NULL
    , callEndedByAgent" BOOLEAN NOT NULL
);
'''

dim_dates='''
CREATE TABLE IF NOT EXISTS staging.dim_dates(
    days TIME(0) WITHOUT TIME ZONE NOT NULL
    , hours TIME(0) WITHOUT TIME ZONE NOT NULL
    , minutes TIME(0) WITHOUT TIME ZONE NOT NULL
    , seconds TIME(0) WITHOUT TIME ZONE NOT NULL
);
'''

dim_agents='''
CREATE TABLE IF NOT EXISTS staging.dim_agents(
    agentID INTEGER PRIMARY KEY NOT NULL
    , agentsGradeLevel" VARCHAR(255) NOT NULL
);
'''


## KPI
dim_kpi='''
CREATE TABLE "ft_agents_kpi"(
    id INTEGER NOT NULL,
    , agent_id" INTEGER NOT NULL
    , totalCallDuration" TIME(0) WITHOUT TIME ZONE NOT NULL
    , averageCallDuration" TIME(0)
    , agentGradeLevel" TEXT 
);
'''


#select statements that make up KPI Table creation
'''
    Select agent_id, assignto, count(callID) from ft_call
    Where (select count(status) from dim_caller where status=CLOSED or “RESOLVED” Group by agentID)
    Join dim_caller 
    On ft_call.callerID=dim_caller.callerID
'''
