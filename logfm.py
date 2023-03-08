import os
import subprocess

def count_logs(paths_list):
    for line in paths_list:
        print(f"Changing directory to {line}")
        new_work_dir = os.path.join(r'/home/cybellum/PSA/psa', line)
        os.chdir(new_work_dir)
        print(f"Running 'poetry lock' in {new_work_dir}")
        subprocess.run(['poetry', 'lock'])
        print(f"Finished running 'poetry lock' in {line}\n")

paths_list = [
    "AuxilaryScripts/dev_ops/cythonization_validations",
    "Builder/OSTreeBuilder",
    "ComponentManager/BatProcessor",
    "ComponentManager/ComponentDataManager",
    "ComponentManager/ComponentIdentifier",
    "ComponentManager/FilterContext",
    "ComponentManager/FilterContextMetadata",
    "CybellumClient/CybellumClientBase",
    "Deploy/PythonObfuscator",
    "DigitalTwinManager/AnalysisTools/analysis_tools/ConfigurationsIdentifier",
    "DigitalTwinManager/AnalysisTools/analysis_tools/DwarfParser",
    "DigitalTwinManager/AnalysisTools/analysis_tools/InterfacesIdentifier",
    "DigitalTwinManager/AnalysisTools/analysis_tools/JohnTheRipper",
    "DigitalTwinManager/AnalysisTools/analysis_tools/KernelCompilationFlagsIdentifier",
    "DigitalTwinManager/AnalysisTools/analysis_tools/KeyCryptoIdentifier",
    "DigitalTwinManager/AnalysisTools/analysis_tools/ProprietaryIdentifier",
    "DigitalTwinManager/AnalysisTools/analysis_tools/ProprietaryIdentifierConfigurations",
    "DigitalTwinManager/AnalysisTools/analysis_tools/StringIdentifier",
    "DigitalTwinManager/AnalysisTools/analysis_tools/WindowsCredentialsDumper",
    "DigitalTwinManager/DtmAnalysisWorker",
    "DigitalTwinManager/DtmAnalysisWorkerTests",
    "DigitalTwinManager/DtmMicroservice",
    "DigitalTwinManager/DtmMicroserviceClient",
    "DigitalTwinManager/DtmMicroserviceCommon",
    "DigitalTwinManager/DtmMicroserviceTest",
    "DigitalTwinManager/DtmModels",
    "DigitalTwinManager/WorkerCommon",
    "E2E",
    "Foundation/ArchitectureIdentifier",
    "Foundation/CPEDbModels",
    "Foundation/CPEParser",
    "Foundation/CyYara",
    "Foundation/CybellumDb",
    "Foundation/CybellumDbModels",
    "Foundation/CybellumLib/v3",
    "Foundation/CybellumSharedDbModels",
    "Foundation/EntropyCalculation",
    "Foundation/ExcelExporter",
    "Foundation/FileSystemIdentifier",
    "Foundation/FileType",
    "Foundation/JiraControl",
    "Foundation/KubernetesManager",
    "Foundation/Microservice",
    "Foundation/MicroserviceClient",
    "Foundation/MicroserviceDatabaseExtension",
    "Foundation/PackageIdentifier",
    "Foundation/RabbitEvents",
    "Foundation/SharedDefinitions",
    "Foundation/SlackNotifier",
    "Foundation/WindowsRegistryParser",
    "JSONServer/JSONServerMicroserviceClient"
]

count_logs(paths_list)
