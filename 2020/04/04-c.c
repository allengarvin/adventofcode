#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>

char *read_file(char *fn) {
    FILE *fd;
    struct stat buf;
    char *contents;

    if( !(fd = fopen(fn, "r")) ) {
        printf("%s: cannot find\n", fn);
        exit(1);
    }
    stat(fn, &buf);
    
    contents = (char *) malloc(buf.st_size + 1);
    if( fread(contents, 1, buf.st_size, fd) != buf.st_size ) {
        printf("%s: problem reading\n", fn);
        exit(1);
    }
    return contents;
}

int count_splits(char *s) {
    int cnt = 0;

    for( int i=0; i<strlen(s); i++ )
        if( s[i] == '\n' && s[i+1] == '\n' )
            cnt++;
    return cnt;
}

char **split_file(char *s, int nn) {
    char **r, *last;
    int i, j, r_ptr = 0, len;

    r = (char **) malloc(nn * sizeof(char *) + 1);
    r[r_ptr++] = s;

    len = strlen(s);
    for( i = 0; i<len; i++ ) {
        if( s[i] == '\n' && s[i-1] == '\n' ) {
            s[i] = 0;
            r[r_ptr++] = &s[i+1];
            i++;
            last = &s[i];
        }
    }
    for( i=0; i<len; i++ )
        if( s[i] == '\n' )
            s[i] = ' ';
    r[r_ptr++] = last;
    return r;
}

int intp(char c) {
    return c >= '0' && c <= '9';
}    

int hexp(char c) {
    return (c >= '0' && c <= '9') || (c >= 'a' && c <= 'f');
}

int test_field(char *field, char *value) {
    int i;

    if( strcmp(field, "byr") == 0 ) {
        i = atoi(value);
        return i >= 1920 && i <= 2002;
    }
    if( strcmp(field, "iyr") == 0 ) {
        i = atoi(value);
        return i >= 2010 && i <= 2020;
    }
    if( strcmp(field, "eyr") == 0 ) {
        i = atoi(value);
        return i >= 2020 && i <= 2030;
    }
    if( strcmp(field, "hgt") == 0 ) {
        char *unit;
        char tmp[20] = { 0 };

        if( strlen(value) < 4 )
            return 0;

        unit = value + strlen(value) - 2;
        strncpy(tmp, value, strlen(value)-2);
        i = atoi(tmp);

        if( strcmp(unit, "in") == 0 )
            return i >= 59 && i <= 76;
        if( strcmp(unit, "cm") == 0 )
            return i >= 150 && i <= 193;
        return 0;
    }
    if( strcmp(field, "cid") == 0 )
        return 1;
    if( strcmp(field, "hcl") == 0 ) {
        if( value[0] != '#' || strlen(value) != 7 )
            return 0;
        for( i=1; i<7; i++ )
            if( !hexp(value[i]) )
                return 0;
        return 1;
    }
    if( strcmp(field, "ecl") == 0 ) {
        if( strcmp(value, "amb") == 0 ) return 1;
        if( strcmp(value, "blu") == 0 ) return 1;
        if( strcmp(value, "brn") == 0 ) return 1;
        if( strcmp(value, "gry") == 0 ) return 1;
        if( strcmp(value, "grn") == 0 ) return 1;
        if( strcmp(value, "hzl") == 0 ) return 1;
        if( strcmp(value, "oth") == 0 ) return 1;
        return 0;
    }
    if( strcmp(field, "pid") == 0 ) {
        if( strlen(value) != 9 )
            return 0;
        for( i=0; i<9; i++ )
            if( !intp(value[i]) )
                return 0;
        return 1;
    }
    return 0;
}

int main() {
    char *con, **records, *r, field[4], value[20];
    int i, j, k, count, valid1 = 0, valid2 = 0;

    con = read_file("04-input.txt");
    count = count_splits(con) + 1;
    records = split_file(con, count);

    field[3] = 0;
    for( int i=0; i<count; i++ ) {
        int field_cnt, cid, good;

        //printf("%s\n", records[i]);

        for( good = 1, cid = 0, field_cnt = 0, r = strtok(records[i], " "); r != NULL; r = strtok(NULL, " ") ) {
            //printf("    %s\n", r);
            strncpy(field, r, 3);
            strncpy(value, r + 4, strlen(r) - 3);

            good &= test_field(field, value);

            if( strcmp(field, "cid") == 0 )
                cid = 1;
            field_cnt++;
        }
        if( field_cnt == 8 || (field_cnt == 7 && !cid) ) {
            valid1++;
            if( good )
                valid2++;
        }
        //puts("-----");
    }
    printf("%d\n", valid1);
    printf("%d\n", valid2);
}
