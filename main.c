#include <stdio.h>
#include <stdlib.h>

int main()
{
    int subject,chapter;
    printf("Welcome to the Engineering Sem-1 Helper \n Please select the subject you would like help with \n");
    printf("1-Physics \n2-Chemistry \n3-Mathematics \n4-Mechanics \n5-Basic Electrical Engineering\n");
    scanf("%d",&subject);
    printf("Select the subject :\n");
    switch(subject){
    case 1:
        printf("1-Quantum Physics \n2-Crystallography \n3-Semiconductor Physics \n4-Interference in Thin Film \n5-Superconductors And Supercapacitors \n6-Engineering Materials And Applications\n");
        scanf("%d",&chapter);
        break;
    case 2:
        printf("1-Atomic and Molecular Structure \n2-Aromatic Systems and their Molecular Systems \n3-Intermolecular Forces And Critical  Phenomena \n4-Gibb's Phase Rule \n5-Polymers \n6-Water\n");
        scanf("%d",&chapter);
        break;
    case 3:
        printf("1-Complex Numbers \n2-Hyperbolic function and Logarithm of Complex Numbers \n3-Partial Differentiation \n4-Applications of Partial Differentiation and Successive differentiation \n5-Matrices \n6-Numerical Solutions of Transcendental Equations and Systemof Linear Equations and Expansion of Function\n");
        scanf("%d",&chapter);
        break;
    case 4:
        printf("11-System of Coplanar Force\n12-Resultant\n21-Equilibrium of System of Coplanar Forces\n22- Equilibrium of Beams\n3-Friction\n4-Kinematics of Particles\n5-Kinematics of Rigid Body\n61-Kinetics of a Particle\n62-Kinetics of a Particle: Work and Energy\n63-Kinetics of a Particle: Impulse and Momentum\n");
        scanf("%d",&chapter);
        break;
    case 5:
        printf("1-DC Circuits\n2-AC Circuits\n3-Three Phase\n4-Transformers\n5-Electrical Machines\n6-Single Phase Induction  Motor\n");
        scanf("%d",&chapter);
        break;
    default:
        printf("Wrong Option!!! Select from 1-5 only(both inclusive)");
    }
    return 0;
}
