---
id: Notes
aliases: []
tags:
  - assignatura/SOI
  - tipus/parcial
---

VMM = Hypervisor
  Qui gestiona les trucades al host del guest

El VMM pot executar diverses MVs amb un sol VMM (?) 
→ SÍ: un sol VMM pot executar diverses MVs simultànies, cada SO guest creient que té el control total

quan el guest vol fer alguna operació privilegiada, el guest ho llença com si el hardware fos seu; el processador captura l'operació (trap) i el VMM l'emula i l'executa de debò (trap-and-emulate, instruccions VT-x a x86)

Type 0: no entenc què és firmware 
→ Firmware = programari gravat dins el propi hardware (ROM/flash), el que s'executa en engegar la màquina **abans** de cap SO (el BIOS/UEFI és firmware). Un hipervisor type 0 viu allà: és el propi firmware el que crea i gestiona les MVs, sense SO ni VMM a part. Poc comú.

Type 1: fa de SO que executa SOs 

Type 2: El normal 
→ hosted: corre com un **procés més** sobre el SO host (VirtualBox, VMware Workstation) — el típic a l'ordinador personal. El disc d'una MV és un fitxer del host.

**Referència: [[T2-Maquines-Virtualitzacio-SO]]**
