# coding='utf8'

import os
import json
import time

from struct import Struct
import const

CCMNT_TOOL_SAVE_ARG = ' -s '
CCMNT_TOOL_OPEN_ARG = ' -f '
CCMNT_TOOL_ENDIAN_ARG = ' -e '
CCMNT_TOOL_BIG_ENDIAN = ' 0 '
CCMNT_TOOL_LITTLE_ENDIAN = ' 1 '

def read_configfile(configfile):
    try:
        with open(configfile) as cf:
            conf = json.load(cf, encoding='utf8')
            return conf
    except IOError as e:
        print('Func err in read_configfile()', e)


def get_root_path(configfile='./config.json'):
    config = read_configfile(configfile)
    ccmnt_tool_path = config['ccmnt_tool_path']
    comm_data_root_path = config['comm_data_root_path']
    save_root_path = config['save_root_path']
    return ccmnt_tool_path, comm_data_root_path, save_root_path


def make_dirs(comm_data_root_path):
    data_save_old_path_dict = {}
    data_save_new_path_dict = {}

    for dirpath, dirnames, filenames in os.walk(comm_data_root_path):
        if dirnames:
            for dn in dirnames:
                if 'dat_' not in dn:
                    save_data_path = os.path.join(dirpath, "dat_" + dn)
                    if not os.path.exists(save_data_path):
                        os.mkdir(save_data_path)
                    data_save_old_path_dict[dn] = save_data_path

        if filenames:
            print dirpath, dirnames, filenames
            for fn in filenames:
                if fn.split('.')[-1:][0] == 'comm':
                    data_save_new_path_dict[os.path.join(dirpath, fn)] = data_save_old_path_dict[
                        dirpath.split('\\')[-1:][0]]
                else:
                    print(fn)

    return data_save_new_path_dict


def run_ccmnt_tool():
    ccmnt_tool_path, comm_data_root_path, save_root_path = get_root_path()
    data_save_path_dict = make_dirs(comm_data_root_path)
    data_save_path_list = []
    for comm_data_path, save_path in data_save_path_dict.items():
        # ccmnt_tool.exe -e 0 -f 11091205.FN_DspLog.comm -s C:\Users\10203524\Desktop\PHY_DATA\
        ccmnt_cmd = ccmnt_tool_path + \
                    const.CCMNT_TOOL_ENDIAN_ARG + const.CCMNT_TOOL_BIG_ENDIAN + \
                    const.CCMNT_TOOL_OPEN_ARG + comm_data_path + \
                    const.CCMNT_TOOL_SAVE_ARG + save_path
        os.system(ccmnt_cmd)
        data_save_path_list.append(save_path)
    return data_save_path_list


def read_ue_arg():
    '''
    hhBBBBBBhIiBBBBBBHBBBBHBBHHHBBBBBB
    h WORD16      wGid
    h WORD16      wCRnti
    B UCHAR       ucCel
    B UCHAR       ucScheType
    B UCHAR       ucAckNackIdType
    B UCHAR       ucRepetitionNumber
    B UCHAR       ucRepetitionIndex
    B UCHAR       ucReTranSeqNum
    h WORD16      wCodeBlkSize
    I WORD32      dTbSize
    i SWORD32     sdFreqOff
    B UCHAR       ucMS
    B UCHAR       ucTone
    B UCHAR       ucReOffset
    B UCHAR       ucReNum
    B UCHAR       ucRuEnd
    B UCHAR       ucRuLength
    H WORD16      ucRuStartSfn
    B UCHAR       ucRuNumber
    B UCHAR       ucRuIndex
    B UCHAR       ucCycleIndex
    B UCHAR       ucCycleNumber
    H WORD16      uwCycleStartSfn
    B UCHAR       ucRvIdx
    B UCHAR       ucStartRv
    H UINT16      uwUeTransMs
    H UINT16      uwUeLastMsFlag
    H UINT16      uwUeFirstMsFlag
    B UCHAR       ucUlTransBreak
    B UCHAR       ucCatchFlag
    B UCHAR       ucUEGroupHoppDisabledSwch
    B UCHAR       ucHarqProc
    B UCHAR       ucCycleEndFlag
    B BYTE        ucRuBrokenByPrach
    :return:
    '''
    filepath = '14_0.dat'
    with open(filepath) as fp:
        data = [line.split('\n')[0] for line in fp.readlines() if line.startswith('0x')]
        print data
        data = [int(d, 16) for d in data]
        s = Struct('I'*len(data))
        packed_data = s.pack(*tuple(data))
        us = Struct('HHBBBBBBhIiBBBBBBHBBBBHBBHHHBBBBBB')
        print us.size
        final_data = [i for i in us.unpack(packed_data[:us.size])]
        print final_data
        # print binascii.hexlify(packed_data)


def main():
    # run_ccmnt_tool()
    read_ue_arg()


if __name__ == '__main__':
    st = time.time()
    main()
    et = time.time()
    print 'using time: %s', et - st
