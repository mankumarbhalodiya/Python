import numpy as np

def analyze_z_system_stability(num_coeffs, den_coeffs):

    print("\n--- Z-System Stability Analysis ---\n")

    poles = np.roots(den_coeffs)

    print(f"Denominator Coefficients D(z): {den_coeffs}")
    print(f"System Poles (roots of D(z)=0): {poles}")
    pole_magnitudes = np.abs(poles)
    print(f"Pole Magnitudes: {pole_magnitudes}")

    is_unstable = np.any(pole_magnitudes >= 1)

    if is_unstable:
        stability_result = "Unstable (At least one pole is outside or on the unit circle, |z| >= 1)."
    else:
        stability_result = "Stable (All poles are strictly inside the unit circle, |z| < 1)."

    print(f"\nConclusion: The system is **{stability_result}**.\n")


num = [1]
den = [1, -0.5]

print("Analyzing Example System: H(z) = 1 / (1 - 0.5z^-1)")
analyze_z_system_stability(num, den)
