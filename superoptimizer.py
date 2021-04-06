from dataclasses import dataclass, field
from typing import List


#
# 8 Registers, Values only from -15 to 15
#
@dataclass
class Simulator:
  registers: List[int] = field(default_factory=list)
  carry: bool = False

  def check_overflow(self, reg1):
    if (self.registers[reg1] > 15):
      self.carry = True
      self.registers[reg1] = 16 - self.registers[reg1]

  def _move(self, reg1, reg2, imm):
    self.registers[reg1] = reg2 if imm else self.registers[reg2]

  def _add(self, reg1, reg2, imm):
    self.registers[reg1] += reg2 if imm else self.registers[reg2]
    self.check_overflow(reg1)

  def _adc(self, reg1, reg2, imm):
    self.registers[reg1] += (reg2 if imm else self.registers[reg2]) + (1 if self.carry else 0)
    self.check_overflow(reg1)

  def _and(self, reg1, reg2, imm):
    self.registers[reg1] = self.registers[reg1] & reg2 if imm else self.registers[reg2]

  def _or(self, reg1, reg2, imm):
    self.registers[reg1] = self.registers[reg1] | reg2 if imm else self.registers[reg2]

  def _xor(self, reg1, reg2, imm):
    self.registers[reg1] = self.registers[reg1] ^ reg2 if imm else self.registers[reg2]

  def _neg(self, reg1):
    self.registers[reg1] = ~self.registers[reg1] + 1

  def _sub(self, reg1, reg2, imm):
    self.registers[reg1] -= reg2 if imm else self.registers[reg2]

  def _lsh(self, reg1, imm):
    if self.registers[reg1] & 16 == 16:
      self.carry = True
    self.registers[reg1] <<= imm
    self.registers[reg1] &= 31

  def _rsh(self, reg1, imm):
    if self.registers[reg1] & 1 == 1:
      self.carry = True
    self.registers[reg1] >>= imm


def generate_instrs(method, reg, val, imm, length):
  prog = []
  for _ in range(length):
    prog += [method, reg, val, imm]

def main():
  sim = Simulator([0, 0, 0, 0, 0, 0])
  print(sim)

  instr_list = []
  # dict of inputs to correct outputs to check our program
  testing_outputs = { i : func(i) for i in range(-15,16) }
  methods = ['_move', '_add', '_adc', '_and', '_or', '_xor', '_neg', '_sub', '_lsh', '_rsh']


  while True:


  print(testing_outputs)


def func(x):
  if x > 0:
    return 1
  elif x < 0:
    return -1
  else:
    return 0


if __name__ == '__main__':
  main()



