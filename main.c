#include <stdio.h>
#include <stdlib.h>
void quantphys();
void crystal();
void semicond();
void interfer();
void supercond();
void engg();
void atom();
void aromatic();
void intermolforces();
void gibb();
void polymer();
void water();
void complexno();
void hyperbolic();
void partial();
void successive();
void matrices();
void numericalsys();
void coplanar();
void resultant();
void equicoplanar();
void equibeams();
void friction();
void kinematicspart();
void kinematicsrigid();
void kineticspart();
void workenergy();
void impulse()
void dcbee();
void acbee();
void thrphase();
void transformer();
void electricalmach();
void singphaseinduc();
int main()
{
    int subject,chapter;
    printf("Welcome to the Engineering Sem-1 Helper \n Please select the subject you would like help with \n");
    printf("1-Physics \n2-Chemistry \n3-Mathematics \n4-Mechanics \n5-Basic Electrical Engineering\n");
    scanf("%d",&subject);
    printf("Select the subject :\n");
    switch(subject){
    case 1:
 label1:printf("1-Quantum Physics \n2-Crystallography \n3-Semiconductor Physics \n4-Interference in Thin Film \n5-Superconductors And Supercapacitors \n6-Engineering Materials And Applications\n");
        scanf("%d",&chapter);
        switch(chapter){
        case 1:
            quantphys();
            break;
        case 2:
            crystal();
            break;
        case 3:
            semicond();
            break;
        case 4:
            interfer();
            break;
        case 5:
            supercond();
            break;
        case 6:
            engg();
            break;
        default:
            printf("Wrong Choice. Please reenter value\n");
            goto label1;
        }
        break;
    case 2:
 label2:printf("1-Atomic and Molecular Structure \n2-Aromatic Systems and their Molecular Systems \n3-Intermolecular Forces And Critical Phenomena \n4-Gibb's Phase Rule \n5-Polymers \n6-Water\n");
        scanf("%d",&chapter);
        switch(chapter){
        case 1:
            atom();
            break;
        case 2:
            aromatic();
            break;
        case 3:
            intermolforces();
            break;
        case 4:
            gibb();
            break;
        case 5:
            polymer();
            break;
        case 6:
            water();
            break;
        default:
            printf("Wrong Choice. Please reenter value\n");
            goto label2;
        }
        break;
    case 3:
 label3:printf("1-Complex Numbers \n2-Hyperbolic function and Logarithm of Complex Numbers \n3-Partial Differentiation \n4-Applications of Partial Differentiation and Successive differentiation \n5-Matrices \n6-Numerical Solutions of Transcendental Equations and Systemof Linear Equations and Expansion of Function\n");
        scanf("%d",&chapter);
        switch(chapter){
        case 1:
            complexno();
            break;
        case 2:
            hyperbolic();
            break;
        case 3:
            partial();
            break;
        case 4:
            successive();
            break;
        case 5:
            matrices();
            break;
        case 6:
            numericalsys();
            break;
        default:
            printf("Wrong Choice. Please reenter value\n");
            goto label3;
        }
        break;
    case 4:
 label4:printf("11-System of Coplanar Force\n12-Resultant\n21-Equilibrium of System of Coplanar Forces\n22- Equilibrium of Beams\n3-Friction\n4-Kinematics of Particles\n5-Kinematics of Rigid Body\n61-Kinetics of a Particle\n62-Kinetics of a Particle: Work and Energy\n63-Kinetics of a Particle: Impulse and Momentum\n");
        scanf("%d",&chapter);
        switch(chapter){
        case 11:
            coplanar();
            break;
        case 12:
            resultant();
            break;
        case 21:
            equicoplanar();
            break;
        case 22:
            equibeams();
            break;
        case 3:
            friction();
            break;
        case 4:
            kinematicspart();
            break;
        case 5:
            kinematicsrigid();
            break;
        case 61:
            kineticspart();
            break;
        case 62:
            workenergy();
            break;
        case 63:
            impulse();
            break;
        default:
            printf("Wrong Choice. Please reenter value\n");
            goto label4;
        }
        break;
        case 5:
 label5:printf("1-DC Circuits\n2-AC Circuits\n3-Three Phase\n4-Transformers\n5-Electrical Machines\n6-Single Phase Induction  Motor\n");
        scanf("%d",&chapter);
        switch(chapter){
        case 1:
            dcbee();
            break;
        case 2:
            acbee();
            break;
        case 3:
            thrphase();
            break;
        case 4:
            transformer();
            break;
        case 5:
            electricalmach();
            break;
        case 6:
            singphaseinduc();
            break;
        default:
            printf("Wrong Choice. Please reenter value\n");
            goto label5;
        }
        break;
    default:
        printf("Wrong Option!!! Select from 1-5 only(both inclusive)");
    }
    return 0;
}
