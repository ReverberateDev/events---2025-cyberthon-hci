byte FUN_00101189(byte param_1)

{
  byte local_f;
  int local_c;
  
  local_f = 0;
  for (local_c = 0; local_c < 8; local_c = local_c + 1) {
    local_f = local_f | (byte)(((int)(uint)(byte)((byte)(param_1 << 4) >> 6 |
                                                 (param_1 >> 4 | param_1 << 4) << 2) >>
                                ((byte)local_c & 0x1f) & 1U) << (7 - (byte)local_c & 0x1f));
  }
  return local_f;
}

bool FUN_00101204(long password)

{
  byte bVar1;
  int local_c;
  
  local_c = 0;
  while( true ) {
    if ((&DAT_00102280)[local_c] == '\0') {
      return *(char *)(password + local_c) == '\0';
    }
    bVar1 = FUN_00101189((&DAT_00102280)[local_c]);
    if ((*(char *)(password + local_c) == '\0') ||
       ((int)*(char *)(password + local_c) != (uint)bVar1)) break;
    local_c = local_c + 1;
  }
  return false;
}