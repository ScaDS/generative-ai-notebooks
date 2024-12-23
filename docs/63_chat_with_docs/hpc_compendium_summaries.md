* accessibility.md:
This document is an accessibility statement for the Technische Universität Dresden's websites, outlining the university's efforts to make its online presence barrier-free in accordance with German law, and providing contact information for reporting accessibility issues and seeking redress.

* data_protection_declaration.md:
This document outlines a data protection policy, stating that only IP addresses are collected for error analysis and not shared with third parties unless required by law, and users have the right to request information about their personal data and contact relevant authorities.

* index.md:
This documentation provides information on the High-Performance Computing (HPC) systems and services offered at the Center for Information Services and High-Performance Computing (ZIH) of the Technical University of Dresden, including user guides, contribution guidelines, news, training courses, and support options.

* legal_notice.md:
This document provides a legal notice for a website or repository associated with the Technische Universität Dresden, including contact information and licensing details for documentation and software components.

* access/desktop_cloud_visualization.md:
The NICE Desktop Cloud Visualization (DCV) tool allows users to remotely access OpenGL 3D applications running on ZIH systems using the server's GPUs, with access options including JupyterHub and troubleshooting tips for GPU support.

* access/graphical_applications_with_webvnc.md:
This document provides instructions on how to run graphical applications on ZIH systems using WebVNC, a web-based client that allows users to access graphical user interfaces through a browser, with setup options available via JupyterHub or terminal access.

* access/jupyterhub.md:
The ZIH (Zentrum für Informationsdienste und Hochleistungsrechnen) at TU Dresden provides a JupyterHub service, offering users a simple way to work with Jupyter notebooks on their systems, with features including customizable environments, access to various clusters, and support for multiple programming languages, all accessible through a web-based interface.

* access/jupyterhub_custom_environments.md:
This document provides a step-by-step guide on creating custom environments for JupyterHub, including using Python virtualenv and conda environments, and installing kernels to use preferred Python packages in Jupyter notebooks on various architectures at ZIH systems.

* access/jupyterhub_for_teaching.md:
This document introduces useful features for using JupyterHub in a teaching setting, including cloning repositories with a link, passing spawn options through URL parameters, creating a shared Python environment, and automatically opening notebooks with a single link.

* access/jupyterhub_teaching_example.md:
This document provides a step-by-step guide for lecturers on setting up a Jupyter Lab course using JupyterHub, including creating custom Python environments, cloning repositories, and activating environments for students to use during the course.

* access/jupyterlab.md:
This document provides step-by-step instructions on how to access JupyterLab on various high-performance computing (HPC) clusters, including Alpha Centauri, Barnard, Capella, Romeo, and Visualization, using either port forwarding or X11 forwarding methods.

* access/jupyterlab_user.md:
This document provides instructions on how to install a custom JupyterLab instance on a specific system, noting that support for custom installations will not be provided by the technicians and is currently only supported at "barnard".

* access/key_fingerprints.md:
This document provides a list of valid SSH key fingerprints for various high-performance computing (HPC) clusters and dataport nodes at TU Dresden, which users should verify when connecting to ensure they are accessing the correct server.

* access/overview.md:
The ZIH systems can be accessed through various methods, including SSH, Desktop Cloud Visualization, WebVNC, and JupyterHub, but require a HPC project, login, and often a Virtual Private Network (VPN) connection, particularly when accessing from outside the campus networks.

* access/security_restrictions.md:
The German HPC sites in Gauß Alliance, including ZIH systems, have implemented new security restrictions, such as password changes, updated SSH key requirements, and limited network access, in response to a recent security incident.

* access/ssh_login.md:
This document provides a step-by-step guide on how to connect to the ZIH systems via terminal on Linux, Mac, and Windows operating systems, including setting up SSH keys, configuring default parameters, and enabling X11-forwarding for graphical applications.

* access/ssh_mobaxterm.md:
This document provides a step-by-step guide on how to connect to a remote server using MobaXterm, a terminal emulator for Windows, including downloading and installing the software, configuring local settings, and starting a new SSH session.

* access/ssh_putty.md:
This document provides a step-by-step guide on how to connect to a remote server using PuTTY, a free and open-source terminal emulator, on a Windows system, including downloading and installing PuTTY, starting a new SSH session, and configuring connection details such as SSH keys and X-forwarding.

* application/acknowledgement.md:
The document requests that users of the NHR center at TU Dresden's high-performance computing (HPC) resources acknowledge the usage of these resources in the acknowledgement section of their publications, providing examples of standard acknowledgement phrases in both English and German.

* application/overview.md:
This document provides information and guidelines for researchers to apply for high-performance computing (HPC) resources at the ZIH, including application procedures, terms of use, and eligibility criteria, particularly for those with doctorates from German universities.

* application/project_management.md:
This document provides a guide for HPC project leaders on how to manage their projects, including adding and removing users, monitoring resources, and viewing statistics, through the project management site, which also allows them to appoint a project administrator to handle these technical details.

* application/terms_of_use.md:
The Terms of Use document outlines the rules and guidelines for using the High-Performance Computing (HPC) resources at the Centre for Information Services and High-Performance Computing (ZIH), including data storage, project management, and user responsibilities, with the German version being the only binding version.

* contrib/content_rules.md:
This markdown document outlines the rules and guidelines for creating and contributing to a documentation project, covering aspects such as writing style, markdown syntax, code blocks, and search customization to ensure consistency and quality.

* contrib/contribute_browser.md:
This document outlines the step-by-step process for contributing to the HPC documentation of TU Dresden/ZIH via GitLab's web interface, including preparation, creating a branch, editing and adding articles, submitting for publication, and revision.

* contrib/contribute_container.md:
This markdown document provides a step-by-step guide on how to contribute to the HPC documentation of TU Dresden/ZIH via a local clone of the Git repository, including initial setup, working with the local clone, merging forked repositories, and using tools to ensure quality, such as Docker containers and automated checks for links, spelling, and text format.

* contrib/howto_contribute.md:
This documentation provides guidance on how to contribute to an open-source project, including its technical setup, content rules, Git workflow, and various methods of contribution, such as via issue, web IDE, or local clone, to ensure collaborative and consistent documentation.

* data_lifecycle/data_sharing.md:
This markdown document provides instructions and commands for sharing data with other users or projects, including granting access to files or directories, using Access Control Lists (ACLs), and managing permissions for workspaces.

* data_lifecycle/file_systems.md:
This document provides an overview of the different filesystems available on ZIH systems, including permanent and working filesystems, and offers recommendations for efficient usage, troubleshooting tips, and commands for debugging filesystem issues.

* data_lifecycle/longterm_preservation.md:
This markdown document discusses the importance of long-term preservation of research data, including why it's necessary, what data should be preserved, the role of metadata, and provides guidance on how to archive research data safely at the ZIH (Center for Information Services and High-Performance Computing) of TU Dresden.

* data_lifecycle/lustre.md:
This document provides guidance on good practices for using Lustre filesystems, including minimizing metadata operations, using optimized commands such as `lfs df` and `lfs find`, and monitoring filesystem usage and striping information to maintain optimal performance.

* data_lifecycle/overview.md:
This document outlines best practices for data life cycle management in high-performance computing (HPC) projects, including guidelines for data storage, backup, organization, metadata, data hygiene, and access rights to ensure efficient collaboration and data preservation.

* data_lifecycle/permanent.md:
This document provides guidance on the use of permanent filesystems on a high-performance computing (HPC) system, including rules for usage, quotas, backup policies, and troubleshooting tips to help users manage their data effectively.

* data_lifecycle/working.md:
This document provides an overview of the various filesystems available on ZIH systems, including their capacities, performances, and recommended uses, as well as tips for efficient usage and troubleshooting common filesystem issues.

* data_lifecycle/workspaces.md:
This document discusses the concept of "workspaces" in a high-performance computing (HPC) environment, specifically at the ZIH (Center for Information Services and High Performance Computing) at TU Dresden. A workspace is a temporary directory with an associated expiration date, created on behalf of a user in a certain filesystem, allowing for better management of HPC data by providing a mechanism to allocate and manage storage space for temporary data, with features such as automatic expiration, extension, and restoration of workspaces.

* data_transfer/datamover.md:
The Datamover is a special data transfer machine provided by ZIH for transferring data between ZIH filesystems at high speeds, and it can be utilized through specific commands such as `dtcp`, `dtmv`, and `dtrsync` after logging in to any ZIH HPC system.

* data_transfer/dataport_nodes.md:
This document provides instructions on how to transfer large amounts of data to and from ZIH systems using dataport nodes, which offer higher bandwidth and are accessible via tools such as SCP, SFTP, and Rsync, with guidance for both Linux and Windows users.

* data_transfer/object_storage.md:
This document provides a step-by-step guide on how to transfer data between ZIH systems and object storage (S3) using the `rclone` module, including initial configuration, copying data, and accessing stored files.

* data_transfer/overview.md:
This document provides guidance on data transfer methods at ZIH systems, recommending the use of dataport nodes for external transfers and the Datamover for internal transfers, with references to detailed documentation for each tool.

* jobs_and_resources/alpha_centauri.md:
The Alpha Centauri GPU cluster is a high-performance computing system designed for AI-related computations, featuring 48 physical cores, 8 NVIDIA A100-SXM4 GPUs, and 1 TB RAM per node, with access to various file systems, modules, and tools, including Python virtual environments, JupyterHub, and Singularity containers.

* jobs_and_resources/arm_hpc_devkit.md:
The NVIDIA Arm HPC Developer Kit is a system provided by ZIH for experimentation with Arm-based systems, featuring a GIGABYTE server, Ampere Altra Q80-30 processor, and NVIDIA A100 GPUs, among other components, and can be accessed via SSH for testing and development purposes.

* jobs_and_resources/binding_and_distribution_of_tasks.md:
This document provides guidance on using Slurm's binding and distribution strategies to optimize the placement of tasks and threads on cores, sockets, and nodes, which can significantly impact the execution time of applications.

* jobs_and_resources/capella.md:
The Lenovo multi-GPU cluster "Capella" is a high-performance computing system installed for AI-related computations and traditional HPC simulations, fully integrated into the ZIH HPC infrastructure and featuring advanced hardware, software, and storage capabilities.

* jobs_and_resources/checkpoint_restart.md:
This markdown document discusses the concept of checkpointing in high-performance computing (HPC) systems, which involves saving the state of a running process to a file so that it can be restarted from where it left off in case of a failure, and provides instructions on how to use the Distributed Multi-Threaded Check-Pointing (DMTCP) tool to implement checkpointing on certain HPC systems.

* jobs_and_resources/hardware_overview.md:
The ZIH systems offer high-performance computing (HPC) resources, comprising six homogeneous clusters with over 100,000 CPU cores and a peak performance of more than 1.5 quadrillion floating-point operations per second, tailored to support data-intensive computing, Big Data analytics, and artificial intelligence methods.

* jobs_and_resources/julia.md:
The SMP Cluster Julia is a high-performance computing resource featuring a large shared memory node, specifically the HPE Superdome Flex, which is well-suited for data-intensive applications and equipped with fast NVMe storage for optimal performance.

* jobs_and_resources/mpi_issues.md:
This document outlines known issues with Message Passing Interface (MPI) implementations, specifically with Open MPI, including performance losses, incorrect resource distribution, and segmentation faults, along with workarounds and solutions for these problems.

* jobs_and_resources/nvme_storage.md:
This document describes the configuration of 90 NVMe storage nodes, each equipped with Intel NVMe SSDs, InfiniBand links, Intel Xeon processors, and RAM, capable of high-speed data transfer.

* jobs_and_resources/overview.md:
This markdown document provides an introduction to the high-performance computing (HPC) resources and jobs at the ZIH, including an overview of the available hardware, how to select suitable hardware for specific applications, and guidelines for submitting jobs, managing memory and runtime limits, and utilizing software and data processing capabilities.

* jobs_and_resources/power9.md:
The GPU Cluster Power9 is a standalone cluster, originally installed in 2018, that has been re-engineered with its own Slurm batch system and login nodes, featuring Power9 architecture and NVIDIA Tesla V100 GPUs, designed for AI, analytics, and data-intensive workloads.

* jobs_and_resources/romeo.md:
The CPU Cluster Romeo is a general-purpose cluster based on AMD Rome CPUs, now a standalone system with its own Slurm batch system and login nodes, offering 128 physical cores and 512 GB of main memory per node, with specific usage guidelines and notes on compatibility with Intel compilers and optimization flags.

* jobs_and_resources/slurm.md:
Here is a one-sentence summary of the markdown document in English:

The document provides a comprehensive guide on using the Slurm batch system for resource management and job scheduling at the ZIH, covering topics such as job submission, interactive and batch jobs, job files, and managing and controlling jobs.

* jobs_and_resources/slurm_examples.md:
This markdown document provides examples and guidelines for submitting various types of jobs, including parallel jobs, exclusive jobs, array jobs, and chain jobs, to a Slurm workload manager, along with explanations of the necessary options and parameters to use in each case.

* jobs_and_resources/slurm_examples_with_gpu.md:
This document provides guidance on requesting and utilizing GPU resources through the Slurm batch system, including examples of job scripts for requesting GPUs, limitations on GPU job allocations, and running multiple GPU applications simultaneously in a batch job.

* jobs_and_resources/slurm_generator.md:
This markdown document describes a Slurm Job File Generator, a tool that helps users create job files for submitting jobs to a High-Performance Computing (HPC) cluster using the Slurm workflow manager.

* jobs_and_resources/slurm_limits.md:
The ZIH systems have resource limits, including runtime and memory limits, to ensure efficient use of compute nodes, and users are advised to submit jobs with estimated runtime and memory requirements to avoid automatic killing or cancellation of their jobs.

* quickstart/getting_started.md:
This markdown document provides a comprehensive guide for new users to get started with using the High Performance Computing (HPC) systems at the ZIH, including applying for a login, accessing the systems, transferring code and data, accessing software, and running parallel HPC jobs.

* software/big_data_frameworks.md:
This document provides a guide on using Big Data analytics frameworks, including Apache Spark, Apache Flink, and Apache Hadoop, on the ZIH systems, covering topics such as loading software modules, configuring and starting clusters, running interactive and batch jobs, and using Jupyter notebooks.

* software/building_software.md:
To build software efficiently, it's recommended to use a job with a separate build directory in the `/data/horse` filesystem, rather than compiling directly in the read-only `/projects` filesystem, and then install the software back to `/projects` from the login node.

* software/cfd.md:
This document provides an overview of Computational Fluid Dynamics (CFD) applications available on a system, including OpenFOAM, Ansys CFX, Ansys Fluent, ICEM CFD, and STAR-CCM+, along with examples of job scripts and usage instructions for each application.

* software/cicd.md:
The ZIH systems provide a GitLab Runner that enables users to run GitLab pipelines on their HPC infrastructure, allowing for continuous building, testing, and benchmarking of HPC software in its target environment.

* software/compilers.md:
This document provides an overview of the compilers and flags available on the ZIH system, including GNU, Clang, Intel, and PGI compilers, and explains how to use various flags to optimize code for performance, debugging, and specific architectures.

* software/containers.md:
This markdown document describes the use of Singularity, a containerization platform, on ZIH systems, including its benefits, installation, container creation, and usage, with the goal of allowing users to run their applications in a consistent and controlled environment without requiring root privileges.

* software/custom_easy_build_environment.md:
This document provides a step-by-step guide on how to use EasyBuild to install custom software modules on a cluster, including setting up a workspace, loading the necessary modules, configuring EasyBuild, searching for and building EasyConfigs, and troubleshooting common issues.

* software/data_analytics.md:
This document provides an overview of the data analytics tools and resources available on ZIH systems, including various software packages, frameworks, and environments, as well as guidance on data transfer, storage, and collaborative work.

* software/data_analytics_with_python.md:
This markdown document provides a comprehensive guide to using Python for data analytics on the ZIH system, covering topics such as setting up Python environments, using Jupyter notebooks, parallel computing with libraries like Pandas and Dask, and utilizing MPI for Python (mpi4py) for message passing and parallel computing.

* software/data_analytics_with_r.md:
This markdown document provides a comprehensive guide to data analytics with R, covering topics such as R console, JupyterHub, RStudio, package installation, deep learning, and parallel computing, with examples and code snippets to help users get started with data analysis using R.

* software/data_analytics_with_rstudio.md:
This document provides an overview of using RStudio, an integrated development environment for R, on ZIH systems, including the option to run it directly in the browser through JupyterHub.

* software/debuggers.md:
This document provides an overview of debugging techniques and tools available at ZIH systems, including GNU Debugger (GDB) and Arm DDT, with specific guidance on debugging serial, multi-threaded, and MPI-parallel programs, as well as memory debugging using tools like Valgrind.

* software/distributed_training.md:
This markdown document discusses distributed training for machine learning models, including data parallelism and model parallelism, and provides examples and guides for implementing distributed training using TensorFlow, PyTorch, and Horovod on high-performance computing systems.

* software/energy_measurement.md:
The Intel Haswell nodes of the ZIH system are equipped with power instrumentation that allows for the recording and accounting of power dissipation and energy consumption data, which can be accessed through various interfaces, including command line tools, Slurm tools, and a C API.

* software/fem_software.md:
This markdown document provides an overview of various finite element method (FEM) software packages available on ZIH systems, including Abaqus, Ansys, COMSOL Multiphysics, and LS-DYNA, with instructions on how to use them interactively or in batch mode, along with examples and tips for efficient utilization.

* software/gpu_programming.md:
This markdown document provides a comprehensive guide to GPU programming on a high-performance computing (HPC) system, covering topics such as available GPUs, using GPUs with Slurm, directive-based GPU programming with OpenACC and OpenMP, native GPU programming with CUDA, and performance analysis using various NVIDIA tools, including nvprof, Visual Profiler, Nsight Systems, and Nsight Compute.

* software/hyperparameter_optimization.md:
Here is a one-sentence summary of the markdown document in English:

The OmniOpt tool is a hyperparameter optimization software that can be used to optimize the performance of various applications, including classical simulations and machine learning algorithms, and is demonstrated through a example use case of optimizing a neural network on the MNIST fashion dataset.

* software/licenses.md:
This document provides information and guidelines for users who want to install and use their own software licenses on ZIH systems, including how to configure the license server and adjust license settings using environment variables.

* software/lo2s.md:
The lightweight node-level performance monitoring tool `lo2s` creates parallel OTF2 traces, providing a comprehensive view of both application and system performance, and can operate in either process monitoring or system monitoring mode to track thread execution, system metrics, and other relevant data.

* software/machine_learning.md:
This document provides an introduction to running machine learning applications on ZIH systems, covering topics such as recommended GPU clusters, loading modules, using Python and R for machine learning, working with Jupyter Notebooks, using containers, and accessing additional libraries and datasets for machine learning tasks.

* software/mathematics.md:
This document provides an overview of the applications of mathematics, specifically focusing on the computing environments Mathematica and MATLAB, including their installation, configuration, and usage on a high-performance computing system, as well as examples of how to use them for parallel computing and batch processing.

* software/math_libraries.md:
This document provides an overview of various high-quality mathematics libraries available for use, including BLAS, LAPACK, ScaLAPACK, AOCL, MKL, and others, which offer efficient and optimized implementations of linear algebra and other mathematical functions for different hardware architectures.

* software/modules.md:
The document describes the environment modules system used on High-Performance Computing (HPC) systems at ZIH, which manages software usage by providing a dynamic modification of a user's environment, allowing for easy switching between different versions of installed software packages and libraries.

* software/mpi_usage_error_detection.md:
The document describes how to use the MUST (MPI Incorrect Usage Checker) tool to check the correctness of MPI (Message Passing Interface) applications, which is a standard for parallel computing, and provides a step-by-step guide on how to set up and run MUST on an HPC system to detect MPI usage errors.

* software/nanoscale_simulations.md:
This markdown document provides an overview of various nanoscale simulation software packages available on a high-performance computing system, including ABINIT, CP2K, CPMD, GAMESS, Gaussian, GROMACS, LAMMPS, NAMD, ORCA, Siesta, and VASP, along with instructions on how to access and use each package.

* software/ngc_containers.md:
This document describes how to use NVIDIA GPU-accelerated containers (NGC containers) for deep learning on the ZIH system, including how to run containers on a single GPU, multiple GPUs, and multiple nodes, as well as the advantages and limitations of using NGC containers.

* software/overview.md:
This document provides an overview of the environment and software used on ZIH systems, including the user environment, software environment, and various options for working with software, such as modules, Jupyter Notebook, and containers.

* software/papi.md:
This document provides an introduction to using the Performance Application Programming Interface (PAPI) to read CPU performance counters, including its basic usage, high-level and low-level APIs, and examples of how to instrument applications and use PAPI tools on ZIH systems.

* software/performance_engineering_overview.md:
This document provides an overview of performance engineering, a process of ensuring that computing systems meet the expected performance requirements, and describes various tools and techniques used in this field, including instrumentation, measurement, analysis, and presentation of performance data.

* software/perf_tools.md:
This document provides an overview of the Linux `perf` command, a performance analysis tool that allows users to sample applications, read performance counters, and identify performance bottlenecks, with tutorials and examples for users and administrators on how to use `perf stat`, `perf record`, `perf report`, `perf script`, and `perf top` commands.

* software/pika.md:
This document describes how to use PIKA, a hardware performance monitoring stack, to track and analyze Slurm jobs on high-performance computing systems, providing a web interface to visualize and understand job efficiency and performance metrics.

* software/power_ai.md:
This document provides an overview of the PowerAI framework for machine learning, including links to various documentation sources, user guides for specific technologies such as TensorFlow and PyTorch, and information on the PowerAI container, all specific to version 1.5.4 and applicable only to the Power9 cluster.

* software/private_modules.md:
This document describes how to set up and use private modules, which allow users to load their own installed software packages into their environment and manage different versions without conflicts, for either individual users or project groups.

* software/python_virtual_environments.md:
This markdown document provides guidance on using Python virtual environments on the ZIH system, including creating and managing environments with `virtualenv` and `conda`, as well as persisting environments for future use.

* software/pytorch.md:
This document provides an overview of using PyTorch, an open-source machine learning framework, on a cluster, including how to load modules, create virtual environments, import PyTorch, and migrate scripts from CPU to GPU, as well as troubleshooting tips and caveats to consider when working with PyTorch.

* software/scorep.md:
The Score-P measurement infrastructure is a scalable tool suite for profiling, event tracing, and online analysis of HPC applications, which can be easily used by prepending the Score-P wrapper to compile and link commands, and allows for configuration of various parameters via environment variables to record profiles and/or event traces.

* software/singularity_power9.md:
This document provides guidance on building and using Singularity containers on the Power9 architecture at ZIH systems, including a recommended workflow, command-line tools, and troubleshooting tips for common issues like filesystem access and SSH key management.

* software/singularity_recipe_hints.md:
This markdown document provides a collection of recipes and hints for working with Singularity, a container platform, including example definitions for creating containers, running GUI applications, using hardware acceleration, and managing temporary and cache directories.

* software/software_development_overview.md:
This markdown document provides an overview of software development and tools on the ZIH systems, covering topics such as compiling code, using libraries, debugging, and optimizing performance, along with helpful hints and questions to consider for ensuring reliable and efficient code.

* software/spec.md:
This document provides guidance on using the SPEChpc 2021 benchmark suite to evaluate the performance of various high-performance computing (HPC) systems, including instructions on installation, configuration, execution, and troubleshooting of common issues.

* software/tensorboard.md:
This document provides a guide on how to use TensorBoard, a visualization toolkit for TensorFlow, to inspect model training, either through JupyterHub or by loading the TensorFlow module environment on a compute node, and accessing it via a web interface.

* software/tensorflow.md:
This document provides an overview of using neural networks with TensorFlow, a free open-source software library, on a cluster, including installation, usage, and compatibility information, as well as examples of working with TensorFlow in various environments such as JupyterHub, containers, and with programming languages like Python and R.

* software/utilities.md:
This document provides an overview of various utilities and tools available on the ZIH systems to make working with them more comfortable, including tmux, lstopo for architecture information, and tools for working with large archives and compressed files, such as rapidgzip and ratarmount.

* software/vampir.md:
This markdown document provides a comprehensive guide on using Vampir, a graphical analysis framework for studying the course of events in parallel programs, including its introduction, setup, usage, and advanced features such as VampirServer and port forwarding.

* software/virtual_desktops.md:
This document provides a guide on how to use WebVNC or DCV to run GUI applications on high-performance computing (HPC) resources, including steps to launch and reconnect to virtual desktops, as well as terminate remote sessions.

* software/virtual_machines.md:
This markdown document provides instructions and guidelines for users to create and access virtual machines (VMs) on ZIH systems, specifically for building Singularity containers on Power9 and x86 architectures.

* software/visualization.md:
This document provides a guide on using ParaView, an open-source data analysis and visualization application, on the ZIH systems at TU Dresden, covering both interactive and batch modes, as well as the use of GPUs for offscreen rendering.

* software/zsh.md:
This document introduces ZSH (z-shell) as an alternative shell to Bash, highlighting its convenience features, such as themes, auto-completion, syntax highlighting, and typo correction, and provides examples of useful plugins and configurations, particularly for use on ZIH systems.

* support/support.md:
The user support document outlines the process for requesting help with HPC systems at TU Dresden, including how to create a ticket via email and attend open Q&A sessions for troubleshooting and guidance.

