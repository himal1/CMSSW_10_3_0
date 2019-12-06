from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'TTree_13TeV_SingleMuon2018AZUpsilonJpsiNoTrigger_Compact'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'makeRealPATEvents_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.outputFiles = ['SingleMuonRun2018A_17Sept2018_ZJpsiUpsilonNoTriggerCompact.root']
config.Data.inputDBS = 'global'
config.Data.inputDataset = '/SingleMuon/Run2018A-17Sep2018-v2/AOD'
#config.Data.outputPrimaryDataset = 'DoubleJPsiToMuMu_RAWSIM_SPS_LO_may2016_largetest_FNAL'
config.Data.lumiMask = 'Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON_MuonPhys.txt'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 100
#NJOBS = 500  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = -1
config.Data.outLFNDirBase = '/store/user/hacharya/DataFiles/'
config.Data.publication = False
config.Site.storageSite ='T3_US_FNALLPC'
