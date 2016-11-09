cdef extern from "ast.h":
	ctypedef struct AstKeyMap:
		pass
	AstKeyMap* astKeyMap(const char *options, ...)
	void astMapPut0D(AstKeyMap *this, const char *key, double value, const char *comment)
	void astMapPut0I(AstKeyMap *this, const char *key, int value, const char *comment)
	void astMapPut0C(AstKeyMap *this, const char *key, const char *value, const char *comment)
	int astMapGet0I(AstKeyMap *this, const char *key, int *value)
	int astMapGet0D(AstKeyMap *this, const char *key, double *value)
	int astMapGet0C(AstKeyMap *this, const char *key, const char **value)

cdef extern from "star/hds_types.h":
	ctypedef struct HDSLoc:
		pass

cdef extern from "sae_par.h":
	pass

cdef extern from "cupid.h":
	int CUPID__DOUBLE
	void cupidSumClumps(int type, void *input, int ndim, int *lbnd, int *ubnd,
						int nel, HDSLoc *obj, float *rmask, void *out,
						const char *method, int *status)
	HDSLoc *cupidGaussClumps(int type, int ndim, int *slbnd, 
							 int *subnd, void *ipd, double *ipv,
							 double rms, AstKeyMap *config, int velax,
							 double beamcorr[3], int *status)

	HDSLoc *cupidClumpFind(int type, int ndim, int *slbnd, int *subnd,
						   void *ipd, double *ipv, double rms, 
						   AstKeyMap *config, int velax, int perspectrum,
						   double beamcorr[3], int *backoff, int *status)

	HDSLoc *cupidFellWalker(int type, int ndim, int *slbnd, int *subnd,
							void *ipd, double *ipv, double rms,
							AstKeyMap *config, int velax, int perspectrum,
							double beamcorr[3], int *status)
	HDSLoc *cupidReinhold(int type, int ndim, int *slbnd, int *subnd,
						  void *ipd, double *ipv, double rms, 
						  AstKeyMap *config, int velax, double beamcorr[3],
						  int *status)