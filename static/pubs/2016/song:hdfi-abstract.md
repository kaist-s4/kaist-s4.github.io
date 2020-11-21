Memory corruption vulnerabilities are the root cause of many
modern attacks. Existing defense mechanisms are inadequate; in
general, the software-based approaches are not efficient and the
hardware-based approaches are not flexible. In this paper, we present
hardware-assisted data-flow isolation, or, Hdfi, a new fine-grained
data isolation mechanism that is broadly applicable and very efficient.
Hdfi enforces isolation at the machine word granularity by virtually
extending each memory unit with an additional tag that is defined
by data-flow.  This capability allows Hdfi to enforce a variety of
security models such as the Biba Integrity Model and the Bell--LaPadula
Model. We implemented Hdfi by extending the RISC-V instruction set
architecture (ISA) and instantiating it on the Xilinx Zynq ZC706
evaluation board. We ran several benchmarks including the SPEC CINT
2000 benchmark suite.  Evaluation results show that the performance
overhead caused by our modification to the hardware is low (<2%). We
also developed or ported several security mechanisms to leverage
Hdfi, including stack protection, standard library enhancement,
virtual function table protection, code pointer protection, kernel
data protection, and information leak prevention.  Our results show
that Hdfi is easy to use, imposes low performance overhead, and allows
us to create more elegant and more secure solutions.
